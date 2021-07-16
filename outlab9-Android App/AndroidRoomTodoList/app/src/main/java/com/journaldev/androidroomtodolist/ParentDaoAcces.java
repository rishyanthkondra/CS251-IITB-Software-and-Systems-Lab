package com.journaldev.androidroomtodolist;

import android.arch.persistence.room.Dao;
import android.arch.persistence.room.Delete;
import android.arch.persistence.room.Insert;
import android.arch.persistence.room.Query;
import android.arch.persistence.room.Update;

import java.util.List;

@Dao
public interface ParentDaoAcces{

    @Insert
    long insertParent(Parent parent);

    @Insert
    void insertParentList(List<Parent> parentList);

    @Query("SELECT pilla FROM " + MyDatabase.TABLE_NAME_PARENT + " WHERE ayya = :thalli")
    List<String> fetchPilla(String thalli);

    @Query("SELECT * FROM " + MyDatabase.TABLE_NAME_PARENT+ " WHERE pilla = :bujji")
    Parent fetchPillabyname(String bujji);

    @Update
    int updatePilla(Parent parent);
}
