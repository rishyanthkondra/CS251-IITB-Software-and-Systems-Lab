package com.journaldev.androidroomtodolist;

import android.content.Intent;
import android.support.v7.widget.CardView;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

import static com.journaldev.androidroomtodolist.MainActivity.NEW_TODO_REQUEST_CODE;

public class SubSubRecycler extends RecyclerView.Adapter<SubSubRecycler.ViewHolder> {

    private List<Todo> todoList;
    private SubSubRecycler.ClickListener clickListener;
    private static int b = -1;
    int mposition;

    public SubSubRecycler(ClickListener clickListener) {
        this.clickListener = clickListener;
        todoList = new ArrayList<>();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {

        public TextView txtName;
        public TextView txtNo;
        public TextView txtDesc;
        public TextView txtCategory;
        public CardView cardView;
        public Button btnButton1;

        public ViewHolder(View view) {
            super(view);

            txtNo = view.findViewById(R.id.txtNo);
            btnButton1= view.findViewById(R.id.button5);
            txtName = view.findViewById(R.id.txtName);
            txtDesc = view.findViewById(R.id.txtDesc);
            txtCategory = view.findViewById(R.id.txtCategory);
            cardView = view.findViewById(R.id.cardView);
            cardView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Log.d("fo","asdfg");
                    //clickListener.launchIntent(todoList.get(getAdapterPosition()).todo_id,todoList.get(getAdapterPosition()).name);
                    b=1;
                    onBindViewHolder(SubSubRecycler.ViewHolder.this,mposition);
                }
            });
        }
    }



    @Override
    public SubSubRecycler.ViewHolder onCreateViewHolder(ViewGroup parent,
                                                            int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.day_recycler, parent, false);
        SubSubRecycler.ViewHolder viewHolder = new SubSubRecycler.ViewHolder(view);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(final SubSubRecycler.ViewHolder holder, int position) {
        Log.d("debug","please");
        final Todo todo = todoList.get(position);
        holder.txtName.setText(todo.name);
        holder.txtNo.setText("#" + String.valueOf(todo.todo_id));
        final boolean isExpanded = b==1;
            holder.txtDesc.setText(todo.description);
        holder.txtCategory.setText(todo.category);
        holder.btnButton1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                clickListener.launchIntent(todo.todo_id,todo.name);
                //Log.d("fo","asdfg");
                //startActivityForResult(new Intent(DayRecyclerAdapter.this, TodoNoteActivity.class).putExtra("PLEASE","Zen"), NEW_TODO_REQUEST_CODE);
            }
        });
        holder.cardView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("fo","asdfg");
                //clickListener.launchIntent(todoList.get(getAdapterPosition()).todo_id,todoList.get(getAdapterPosition()).name);
                b=1;
                onBindViewHolder(holder,holder.getAdapterPosition());
                b=0;
            }
        });

        mposition=position;
    }

    @Override
    public int getItemCount() {
        return todoList.size();
    }


    public void updateTodoList(List<Todo> data) {
        todoList.clear();
        todoList.addAll(data);
        notifyDataSetChanged();
        System.out.print("hello");
    }

    public void addRow(Todo data) {
        todoList.add(data);
        notifyDataSetChanged();
    }



    public interface ClickListener {
        void launchIntent(int id,String Name);
    }
}


