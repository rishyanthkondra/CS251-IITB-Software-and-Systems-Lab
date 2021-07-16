package com.journaldev.androidroomtodolist;

import android.annotation.SuppressLint;
import android.arch.persistence.room.Room;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.NavigationView;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;
import java.util.Date;
import java.text.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

import android.support.annotation.NonNull;
import android.support.design.widget.NavigationView;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements RecyclerViewAdapter.ClickListener, AdapterView.OnItemSelectedListener {

    MyDatabase myDatabase;
    RecyclerView recyclerView;
    Spinner spinner;
    RecyclerViewAdapter recyclerViewAdapter;

    private DrawerLayout dl;
    private ActionBarDrawerToggle t;
    private NavigationView nv;
    //FloatingActionButton floatingActionButton;
    private String[] categories = {
            "Home",
            "Day View"
    };

    ArrayList<Todo> todoArrayList = new ArrayList<>();
    ArrayList<Parent> parentArrayList = new ArrayList<>();
    ArrayList<String> spinnerList = new ArrayList<>(Arrays.asList(categories));

    public static final int NEW_TODO_REQUEST_CODE = 200;
    public static final int UPDATE_TODO_REQUEST_CODE = 300;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dl = (DrawerLayout)findViewById(R.id.activity_main);
        t = new ActionBarDrawerToggle(this, dl,R.string.Open, R.string.Close);
        t.setDrawerIndicatorEnabled(true);

        dl.addDrawerListener(t);
        t.syncState();
        Toolbar mToolBar = findViewById(R.id.my_toolbar);


        setSupportActionBar(mToolBar);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        nv = (NavigationView)findViewById(R.id.nv);


        nv.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                int id = item.getItemId();
                switch(id)
                {
                    case R.id.account:
                        startActivityForResult(new Intent(MainActivity.this, MainActivity.class), NEW_TODO_REQUEST_CODE);break;
                    case R.id.settings:
                        startActivityForResult(new Intent(MainActivity.this, Dayview.class), NEW_TODO_REQUEST_CODE);break;
                    default:
                        return true;
                }


                return true;

            }
        });

        initViews();
        myDatabase = Room.databaseBuilder(getApplicationContext(), MyDatabase.class, MyDatabase.DB_NAME).fallbackToDestructiveMigration().build();
        checkIfAppLaunchedFirstTime();
        spinner.setOnItemSelectedListener(this);
        spinner.setSelection(0);

        /**floatingActionButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivityForResult(new Intent(MainActivity.this, TodoNoteActivity.class).putExtra("PLEASE","Zen"), NEW_TODO_REQUEST_CODE);
            }
        });**/

    }

    private void initViews() {

        //floatingActionButton = findViewById(R.id.fab);
        spinner = findViewById(R.id.spinner);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, spinnerList);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);


        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerViewAdapter = new RecyclerViewAdapter(this);
        recyclerView.setAdapter(recyclerViewAdapter);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if(t.onOptionsItemSelected(item)){return true;}
        if (id == R.id.action_favorite) {
            startActivityForResult(new Intent(MainActivity.this, TodoNoteActivity.class).putExtra("PLEASE","Zen"), NEW_TODO_REQUEST_CODE);
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public void launchIntent(int id,String Name) {
        Intent i = new Intent(MainActivity.this, SubActivity.class);
        i.putExtra("id", id);
        i.putExtra("NAME",Name);
        startActivityForResult(i, UPDATE_TODO_REQUEST_CODE);
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {


        if (position == 0) {
            loadAllTodos();
        } else {
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            Date date = new Date();
            String string = sdf.format(date);
            loadFilteredTodos(string);
        }
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }


    @SuppressLint("StaticFieldLeak")
    private void loadFilteredTodos(String category) {
        new AsyncTask<String, Void, List<Todo>>() {
            @Override
            protected List<Todo> doInBackground(String... params) {
                return myDatabase.daoAccess().fetchTodoListByCategory(params[0]);

            }

            @Override
            protected void onPostExecute(List<Todo> todoList) {
                recyclerViewAdapter.updateTodoList(todoList);
            }
        }.execute(category);

    }


    @SuppressLint("StaticFieldLeak")
    private void fetchTodoByIdAndInsert(int id) {
        new AsyncTask<Integer, Void, Todo>() {
            @Override
            protected Todo doInBackground(Integer... params) {
                return myDatabase.daoAccess().fetchTodoListById(params[0]);

            }

            @Override
            protected void onPostExecute(Todo todoList) {
                recyclerViewAdapter.addRow(todoList);
            }
        }.execute(id);

    }

    @SuppressLint("StaticFieldLeak")
    private void loadAllTodos() {
        new AsyncTask<String, Void, List<Todo>>() {
            @Override
            protected List<Todo> doInBackground(String... params) {
                List<String> childs = myDatabase.parentDaoAcces().fetchPilla("Zen");
                List<Todo> ans= new ArrayList<>();
                ans.addAll(myDatabase.daoAccess().fetchSpecificTodos("Zen"));
                for (String temp : childs) {
                    ans.addAll(myDatabase.daoAccess().fetchSpecificTodos(temp));
                }
                return ans;
            }

            @Override
            protected void onPostExecute(List<Todo> todoList) {
                recyclerViewAdapter.updateTodoList(todoList);
            }
        }.execute();
    }

    private void buildDummyTodos() {
        Parent parent;
        Todo todo = new Todo();
        todo.name = "Zen";
        todo.description = "If you chase two rabbits, you catch none.";
        todo.category = "";
        todo.categoryp="";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Acads";
        todo.description = "Padhai ki baatein";
        todo.category = "2019-12-31";
        todo.categoryp = "2019-12-31";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Self improvement";
        todo.description = "Reading list, blogs, exercise, etc.";
        todo.category = "2019-12-30";
        todo.categoryp = "2019-12-30";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Research";
        todo.description = "Pet projects";
        todo.category = null;
        todo.categoryp="";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Hobbies";
        todo.description = "<3";
        todo.category = null;
        todo.categoryp="";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Exercise";
        todo.description = "someday?";
        todo.category = "2021-2-29";
        todo.categoryp="2021-2-29";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Reading list";
        todo.description = "My bucket list:\nHear the Wind Sing\nThe Fountainhead\nAtlas Shrugged\nA prisoner of birth";
        todo.category = null;
        todo.categoryp="2019-12-30";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Origami";
        todo.description = "cranes and tigers";
        todo.category = "2019-10-29";
        todo.categoryp="2019-10-29";

        todoArrayList.add(todo);

        todo = new Todo();
        todo.name = "Drum practice!";
        todo.description = "Aim:\nHallowed be thy name,\nAcid Rain (LTE)";
        todo.category = "2019-10-29";
        todo.categoryp="2019-10-29";

        todoArrayList.add(todo);

        parent = new Parent();
        parent.pilla = "Acads";
        parent.ayya = "Zen";
        parent.dhari = "Z/Acads";
        parentArrayList.add(parent);

        parent = new Parent();
        parent.pilla = "Self improvement";
        parent.ayya = "Zen";
        parent.dhari = "Z/Self improvement";

        parentArrayList.add(parent);

        parent = new Parent();
        parent.pilla = "Research";
        parent.ayya = "Zen";
        parent.dhari = "Z/Research";

        parentArrayList.add(parent);

        parent = new Parent();
        parent.pilla = "Hobbies";
        parent.ayya = "Zen";
        parent.dhari = "Z/Hobbies";

        parentArrayList.add(parent);

        parent = new Parent();
        parent.pilla = "Exercise";
        parent.ayya = "Self improvement";
        parent.dhari = "Z/Exercise";

        parentArrayList.add(parent);

        parent = new Parent();
        parent.pilla = "Reading list";
        parent.ayya = "Self improvement";
        parent.dhari = "Z/Reading list";

        parentArrayList.add(parent);

        parent = new Parent();
        parent.pilla = "Origami";
        parent.ayya = "Hobbies";
        parent.dhari = "Z/Origami";

        parentArrayList.add(parent);

        parent = new Parent();
        parent.pilla = "Drum practice!";
        parent.ayya = "Hobbies";
        parent.dhari = "Z/Drum practice!";

        parentArrayList.add(parent);

        insertPar(parentArrayList);
        insertList(todoArrayList);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK) {

            //reset spinners
            spinner.setSelection(0);

            if (requestCode == NEW_TODO_REQUEST_CODE) {
                long id = data.getLongExtra("id", -1);
                Toast.makeText(getApplicationContext(), "Row inserted", Toast.LENGTH_SHORT).show();
                fetchTodoByIdAndInsert((int) id);

            } else if (requestCode == UPDATE_TODO_REQUEST_CODE) {

                boolean isDeleted = data.getBooleanExtra("isDeleted", false);
                int number = data.getIntExtra("number", -1);
                if (isDeleted) {
                    Toast.makeText(getApplicationContext(), number + " rows deleted", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(getApplicationContext(), number + " rows updated", Toast.LENGTH_SHORT).show();
                }

                loadAllTodos();

            }


        } else {
            //Toast.makeText(getApplicationContext(), "No action done by user", Toast.LENGTH_SHORT).show();
        }
    }

    @SuppressLint("StaticFieldLeak")
    private void insertList(List<Todo> todoList) {
        new AsyncTask<List<Todo>, Void, Void>() {
            @Override
            protected Void doInBackground(List<Todo>... params) {
                myDatabase.daoAccess().insertTodoList(params[0]);

                return null;

            }

            @Override
            protected void onPostExecute(Void voids) {
                super.onPostExecute(voids);
            }
        }.execute(todoList);

    }

    @SuppressLint("StaticFieldLeak")
    private void insertPar(List<Parent> parentList) {
        new AsyncTask<List<Parent>, Void, Void>() {
            @Override
            protected Void doInBackground(List<Parent>... params) {
                myDatabase.parentDaoAcces().insertParentList(params[0]);

                return null;

            }

            @Override
            protected void onPostExecute(Void voids) {
                super.onPostExecute(voids);
            }
        }.execute(parentList);

    }

    private void checkIfAppLaunchedFirstTime() {
        final String PREFS_NAME = "SharedPrefs";

        SharedPreferences settings = getSharedPreferences(PREFS_NAME, 0);

        if (settings.getBoolean("firstTime", true)) {
            settings.edit().putBoolean("firstTime", false).apply();
            buildDummyTodos();
        }
    }
}

