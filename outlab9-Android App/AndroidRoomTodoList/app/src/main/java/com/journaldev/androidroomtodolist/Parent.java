package com.journaldev.androidroomtodolist;
import android.arch.persistence.room.Entity;
import android.arch.persistence.room.Ignore;
import android.arch.persistence.room.*;
import static android.arch.persistence.room.ForeignKey.CASCADE;
import java.io.Serializable;

@Entity(tableName = MyDatabase.TABLE_NAME_PARENT /**, foreignKeys = @ForeignKey(entity = Todo.class,
        parentColumns = "todo_id",
        childColumns = "child_id",
        onDelete = CASCADE)**/)
public class Parent implements Serializable {

    @PrimaryKey(autoGenerate = true)
    public int child_id;

    public String pilla;

    public String ayya;

    public String dhari;

    @Ignore
    public String priority;

}
