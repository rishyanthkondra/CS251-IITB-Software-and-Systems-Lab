package com.journaldev.androidroomtodolist;

import android.annotation.SuppressLint;
import android.arch.persistence.room.Room;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.List;

import android.widget.DatePicker;
import android.app.DatePickerDialog;
import android.widget.Toast;
import android.app.Dialog;

import static com.journaldev.androidroomtodolist.SubSubTaskactivity.NEW_TODO_REQUEST_CODE;

public class TodoNoteActivity extends AppCompatActivity {

    DatePicker datePicker;
    Calendar calendar;
    int day,month,samva;
    int a = 0;
    String dateView = "";
    EditText inTitle, inDesc;
    Button btnDone, btnDelete;
    boolean isNewTodo = false;
    String par;
    String pardat;

    MyDatabase myDatabase;

    Todo updateTodo;
    Parent updateParent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_todo_note);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        calendar = Calendar.getInstance();
        samva = calendar.get(Calendar.YEAR);
        month = calendar.get(Calendar.MONTH);
        day = calendar.get(Calendar.DAY_OF_MONTH);
        inTitle = findViewById(R.id.inTitle);
        inDesc = findViewById(R.id.inDescription);
        btnDone = findViewById(R.id.btnDone);
        btnDelete = findViewById(R.id.btnDelete);

        myDatabase = Room.databaseBuilder(getApplicationContext(), MyDatabase.class, MyDatabase.DB_NAME).build();

        final int todo_id = getIntent().getIntExtra("id", -100);
        par = getIntent().getStringExtra("PLEASE");

        final String sed = getIntent().getStringExtra("NAME");

        if (todo_id == -100)
            isNewTodo = true;

        if (!isNewTodo) {
            fetchTodoById(todo_id);
            btnDelete.setVisibility(View.VISIBLE);
        }

        btnDone.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isNewTodo) {
                    Todo todo = new Todo();
                    todo.name = inTitle.getText().toString();
                    todo.description = inDesc.getText().toString();
                    todo.category = dateView;
                    if(dateView == null || dateView == ""){todo.categoryp = pardat;}


                    Parent parent = new Parent();
                    parent.pilla = inTitle.getText().toString();
                    parent.ayya = par;
                    parent.dhari = "Z/"+inTitle.getText().toString();


                    insertPillalu(parent);
                    insertRow(todo);
                } else {

                    updateTodo.name = inTitle.getText().toString();
                    updateTodo.description = inDesc.getText().toString();
                    if (a == 0){
                    dateView = updateTodo.category;
                        updateTodo.category = dateView;
                    pardat = updateTodo.categoryp;
                    updateTodo.categoryp = pardat;}
                    else{updateTodo.category = dateView;
                    updateTodo.categoryp = dateView;}

                    updateParent.pilla = inTitle.getText().toString();
                    par = updateParent.ayya;
                    updateParent.ayya = par;
                    updateParent.dhari = "Z/"+inTitle.getText().toString();


                    
                    updateRow(updateTodo);
                    updatePillalu(updateParent);
                }
                if(par == "Zen"){startActivityForResult(new Intent(TodoNoteActivity.this, MainActivity.class), NEW_TODO_REQUEST_CODE);}
                else{Intent i = new Intent(TodoNoteActivity.this,SubActivity.class);
                    i.putExtra("id", todo_id);
                    i.putExtra("NAME",par);
                    startActivityForResult(i, NEW_TODO_REQUEST_CODE);}
            }
        });

        btnDelete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                deleteRow(updateTodo);
            }
        });
    }

    @SuppressWarnings("deprecation")
    public void setDate(View view) {
        a=1;
        Log.d("fo","asdfg");
        showDialog(999);
        Toast.makeText(getApplicationContext(), "set the date",
                Toast.LENGTH_SHORT)
                .show();
    }

    private DatePickerDialog.OnDateSetListener myDateListener = new
            DatePickerDialog.OnDateSetListener() {
                @Override
                public void onDateSet(DatePicker arg0,
                                      int arg1, int arg2, int arg3) {
                    // TODO Auto-generated method stub
                    // arg1 = year
                    // arg2 = month
                    // arg3 = day
                    showDate(arg1, arg2+1, arg3);
                }
            };

    @Override
    protected Dialog onCreateDialog(int id) {
        // TODO Auto-generated method stub
        if (id == 999) {
            return new DatePickerDialog(this,
                    myDateListener, samva, month, day);
        }
        return null;
    }


    private void showDate(int year, int month, int day) {
        dateView = new StringBuilder().append(year).append("-")
                .append(month).append("-").append(day).toString();
    }

    @SuppressLint("StaticFieldLeak")
    private void fetchTodoById(final int todo_id) {
        new AsyncTask<Integer, Void, Todo>() {
            @Override
            protected Todo doInBackground(Integer... params) {

                Todo todo1 = myDatabase.daoAccess().fetchTodoListById(params[0]);
                updateParent = myDatabase.parentDaoAcces().fetchPillabyname(todo1.name);
                if(updateParent.ayya == "Zen"){
                    List<String> children = myDatabase.parentDaoAcces().fetchPilla(todo1.name);
                    for (String temp:children){
                        Todo update = myDatabase.daoAccess().fetchAllTodos(temp);
                        if(update!=null){
                            update.categoryp = dateView;
                            Log.d("jnsnvsd","osey");
                            updateRow(update);
                        }
                    }
                }
                return todo1;

            }

            @Override
            protected void onPostExecute(Todo todo) {
                super.onPostExecute(todo);
                inTitle.setText(todo.name);
                inDesc.setText(todo.description);
                //spinner.setSelection(spinnerList.indexOf(todo.category));

                updateTodo = todo;
            }
        }.execute(todo_id);

    }



    @SuppressLint("StaticFieldLeak")
    private void insertRow(Todo todo) {
        new AsyncTask<Todo, Void, Long>() {
            @Override
            protected Long doInBackground(Todo... params) {
                return myDatabase.daoAccess().insertTodo(params[0]);
            }

            @Override
            protected void onPostExecute(Long id) {
                super.onPostExecute(id);

                Intent intent = getIntent();
                intent.putExtra("isNew", true).putExtra("id", id);
                setResult(RESULT_OK, intent);
                finish();
            }
        }.execute(todo);

    }

    @SuppressLint("StaticFieldLeak")
    private void insertPillalu(Parent parent) {
        new AsyncTask<Parent, Void, Long>() {
            @Override
            protected Long doInBackground(Parent... params) {
                return myDatabase.parentDaoAcces().insertParent(params[0]);
            }

            @Override
            protected void onPostExecute(Long id) {
                super.onPostExecute(id);

                Intent intent = getIntent();
                intent.putExtra("isNew", true).putExtra("id", id);
                setResult(RESULT_OK, intent);
                finish();
            }
        }.execute(parent);

    }


    @SuppressLint("StaticFieldLeak")
    private void deleteRow(Todo todo) {
        new AsyncTask<Todo, Void, Integer>() {
            @Override
            protected Integer doInBackground(Todo... params) {
                return myDatabase.daoAccess().deleteTodo(params[0]);
            }

            @Override
            protected void onPostExecute(Integer number) {
                super.onPostExecute(number);

                Intent intent = getIntent();
                intent.putExtra("isDeleted", true).putExtra("number", number);
                setResult(RESULT_OK, intent);
                finish();
            }
        }.execute(todo);

    }


    @SuppressLint("StaticFieldLeak")
    private void updateRow(Todo todo) {
        new AsyncTask<Todo, Void, Integer>() {
            @Override
            protected Integer doInBackground(Todo... params) {
                return myDatabase.daoAccess().updateTodo(params[0]);
            }

            @Override
            protected void onPostExecute(Integer number) {
                super.onPostExecute(number);

                Intent intent = getIntent();
                intent.putExtra("isNew", false).putExtra("number", number);
                setResult(RESULT_OK, intent);
                finish();
            }
        }.execute(todo);

    }

    @SuppressLint("StaticFieldLeak")
    private void updatePillalu(Parent parent) {
        new AsyncTask<Parent, Void, Integer>() {
            @Override
            protected Integer doInBackground(Parent... params) {
                return myDatabase.parentDaoAcces().updatePilla(params[0]);
            }

            @Override
            protected void onPostExecute(Integer number) {
                super.onPostExecute(number);

                Intent intent = getIntent();
                intent.putExtra("isNew", false).putExtra("number", number);
                setResult(RESULT_OK, intent);
                finish();
            }
        }.execute(parent);



    }

}
