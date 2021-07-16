/**
*@file stud_rec.cpp
@brief Creating a database of students information
@details
<pre>
	-Stores  the information of each student in order in an array.
	-Adding student's information to the database.
	-Updating student's record in the database.
	-Deleting student's record from the database.
	-Finding student's average marks from the database.
	-Finding the student with the maximum marks in the database.
	-Finding the student with the minimum marks in the database.
	-View all students records in the database.
	-Search for student record in the database.
</pre>
**/

#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <string.h>
using namespace std;


//!Stores the information of a student.
//!Working of this student is described in detail.
struct student
{//!This stores the ID of the student.
	string stnumber;
	//!This stores the name of the student
	string stname;
	//!This stores the gender of the student
	char sex;
	//!This stores the quiz 1 marks of the student
	float quizz1;
	//!This stores the quiz 2 marks of the student
	float quizz2;
	//!This stores the assignment marks of the student
	float assigment;
	//!This stores the midterm marks of the student
	float midterm;
	//!This stores the final exam marks of the student
	float final;
	//!This stores the total marks of the student
	float total;
	//!This is the item number i.e the number in the array assigned to a student in the student database(stored as an array)
	//!But this is not used anywhere.
	int numberOfitem;
};
int search(struct student st[],string id, int itemcount);
void clean(struct student st[],int deleteitem);
//!This is a menu which shows available options for the user to choose from.
void displaymenu(){
	cout<<"=========================================="<<"\n";
	cout<<" MENU "<<"\n";
	cout<<"=========================================="<<"\n";
	cout<<" 1.Add student records"<<"\n";
	cout<<" 2.Delete student records"<<"\n";
	cout<<" 3.Update student records"<<"\n";
	cout<<" 4.View all student records"<<"\n";
	cout<<" 5.Calculate average score of a student"<<"\n";
	cout<<" 6.Show student who gets the max total score"<<"\n";
	cout<<" 7.Show student who gets the max total score"<<"\n"; 
	cout<<" 8.Find a student by ID"<<"\n"; 
	cout<<" 9.Sort records by TOTAL"<<"\n"; 
}

//!After choosing option 1,this function is called to add record of a student into the database.
/*
	\param st[] -> a student array
	\param itemcount ->  size of st[] to consider
	\return void
*/
void add_rec(struct student st[],int& itemcount){
	again:
	cout<<"\nEnter student's ID:";
	cin>>st[itemcount].stnumber;
	//!Check if the id already exists,and if it exists then should type in a different id
	if(search(st,st[itemcount].stnumber,itemcount)!=-1){
		cout<<"This ID already exists\n";goto again;
	}
	//!After entering a new ID, we enter the remaining information of the student 
	//!into the database(which is a struct 'student' with itemcount as the index pointing to each student.)
	cout<<"Enter student's Name:"; 
	cin>>st[itemcount].stname;
	cout<<"Enter student's Sex(F or M):";cin>>st[itemcount].sex;
	cout<<"Enter student's quizz1 score:";cin>>st[itemcount].quizz1;
	cout<<"Enter student's quizz2 score:";cin>>st[itemcount].quizz2;
	cout<<"Enter student's assigment score:";cin>>st[itemcount].assigment;
	cout<<"Enter student's mid term score:";cin>>st[itemcount].midterm;
	cout<<"Enter student's final score:";cin>>st[itemcount].final;
	st[itemcount].total=st[itemcount].quizz1+st[itemcount].quizz2+st[itemcount].assigment+st[itemcount].midterm+st[itemcount].final;
	//! update the number of items in the database.
	++itemcount;
}
//!To check if a particular student information is already present with the help of an ID.
/*
	\param st[] -> a student array
	\param id -> ID of the student
	\param itemcount ->  size of st[] to consider
	\return void
*/
int search(struct student st[], string id,int itemcount){
	int found =-1;
	for (int i = 0; i < itemcount && found==-1; i++)
	{
		if (st[i].stnumber == id) found=i;
		else found=-1 ;
	}

	return found;
}


//!For viewing information of all students in the database.
/*
	\param st[] -> a student array
	\param itemcount ->  size of st[] to consider
	\return void
*/
void viewall(struct student st[], int itemcount){
	//!First display the column names.
	int i=0;
	cout<<left<<setw(5)<<"ID"<<setw(20)<<"NAME"<<setw(5)<<"SEX"

	<<setw(5)<<"Q1"
	<<setw(5)<<"Q2"<<setw(5)<<"As"<<setw(5)<<"Mi"<<setw(5)<<"Fi"
	<<setw(5)<<"TOTAL"<<"\n";
	cout<<"==============================================\n";
	//!Iterate over the entire database and print each student's details,
	//!including total marks.
	while(i<=itemcount){
		if(st[i].stnumber!=""){
			cout<<left<<setw(5)<<st[i].stnumber<<setw(20)<<st[i].stname<<setw(5)

			<<st[i].sex;
			cout<<setw(5)<<st[i].quizz1<<setw(5)<<st[i].quizz2<<setw(5)<<st[i].assigment
			<<setw(5)<<st[i].midterm<<setw(5)<<st[i]. final<<setw(5)
			<<st[i].total;

			cout<<"\n";
		}
		i=i+1;
	}
}
//!Deleting information of a student from the database.
/*
	\param st[] -> a student array
	\param itemcount ->  size of st[] to consider
	\return void
*/
void delete_rec(struct student st[], int& itemcount){
	
	string id;
	int index;
	if (itemcount > 0)
	{
		cout<<"Enter student's ID:";
		cin>>id;
		index = search(st, id,itemcount); 
		//!Takes ID of a possible student and searches in the database.If the ID is present,
		//!then it goes on to delete all the information of the student using clean function.
		//!After making sure that ID is present,
		if ((index!=-1) && (itemcount != 0)){
			if (index == (itemcount-1)){ 

				clean(st, index);
				--itemcount;

				cout<<"The record was deleted.\n";
			}
			else{ 
				for (int i = index; i < itemcount-1; i++){
					st[i] = st[i + 1];
					clean(st, itemcount);
					--itemcount ;
				}
			}
		}
		else cout<<"The record doesn't exist.Check the ID and try again.\n";
	}
	else cout<<"No record to delete\n";
}
//!To clear the information at a particular position in the database.
/*
	\param st[] -> a student array
	\param index ->  position in the st[] array
	\return void
*/
void clean(struct student st[],int index){
	//Reset all the variables 
	st[index].stnumber = "";
	st[index].stname = "";
	st[index].sex = 'X';
	st[index].quizz1 = 0;
	st[index].quizz2 = 0;
	st[index].assigment = 0;
	st[index].midterm = 0;
	st[index].final = 0;
	st[index].total = 0;
}

//!This can be used to update information of a student if any changes are required,
//!instead of deleting the information and then re-entering it.
/*
	\param st[] -> a student array
	\param itemcount ->  size of st[] to consider
	\return void
*/
void update_rec(struct student st[],int itemcount){
	//!Choose a field which we want to update and then modify it.
	string id;
	int column_index;
	cout<<"Enter student's ID:";
	cin>>id;
	cout<<"Which field you want to update(1-7)?:";
	cin>>column_index;

	int index = search(st, id,itemcount);
	//!Provided the ID exists,we can update it or else generate an error message
	//!informing that There is no such ID and to try again.Note that,we can't update 
	//!multiple columns at the same time. 
	if (index != -1)
	{
		if (column_index == 1){
			cout<<"Enter student's Name:";
			cin>>st[index].stname;
		}

		else if (column_index == 2){
			cout<<"Enter student's Sex(F or M):";
			cin>>st[index].sex;
		}
		else if (column_index == 3){
			cout<<"Enter student's quizz1 score:";
			cin>>st[index].quizz1;
		}
		else if (column_index == 4){
			cout<<"Enter student's quizz2 score:";
			cin>>st[index].quizz2;
		}
		else if (column_index == 5){
			cout<<"Enter student's assigment score:";
			cin>>st[index].assigment;
		}
		else if (column_index == 6){
			cout<<"Enter student's mid term score:";
			cin>>st[index].midterm;
		}
		else if (column_index == 7)	{
			cout<<"Enter student's final score:";
			cin>>st[index].final;
		}
		else cout<<"Invalid column index";
		//!Recalculate the total marks.
		st[index].total = st[index].quizz1 + st[index].quizz2 + st[index].assigment

		+ st[index].midterm + st[index].final;
	}
	else cout<<"The record deosn't exits.Check the ID and try again.";
}
//!Out of all the students, to print the information of the student who has the highest total score.
/*
	\param st[] -> a student array
	\param itemcount ->  size of st[] to consider
	\return void
*/
void showmax(struct student st[], int itemcount){
	float max = st[0].total;
	int index=0;

	if (itemcount >= 2){
		for (int j = 0; j < itemcount-1; ++j)
			if (max < st[j+1].total) {
				max = st[j+1].total;
				index = j+1;
			}
	}
	else if (itemcount == 1){
		index = 0;
		max = st[0].total;
	}
	else 
		cout<<"Not record found!\n";

	if (index != -1) 
		cout<<"The student with ID "<<st[index].stnumber<<" gets the highest score "<<max<<endl;
}
//!Out of all the students, to print the information of the student who has the lowest total score.
/*
	\param st[] -> a student array
	\param itemcount ->  size of st[] to consider
	\return void
*/
void showmin(struct student st[], int itemcount){

	float min = st[0].total;
	int index = 0;

	if (itemcount >= 2){
		for (int j = 0; j < itemcount-1; ++j)
			if (min > st[j+1].total){
				min = st[j+1].total;
				index = j+1;
			}
	}
	else if (itemcount == 1){
		index = 0;
		min = st[0].total;
	}
	else 
		cout<<"No record found!\n";

	if (index != -1) cout<<"The student with ID "<<st[index].stnumber<<" gets the highest score "<<min<<endl;

}
//!Function called when chosen option 8 ,where we find a student with an ID.
/* 
	\param st[] -> a student array
	\param itemcount -> size of st[] to consider
	\return void
*/
void find(struct student st[], int itemcount){
	//!Print the student details,if there exists a student with that ID or else print that no such record exists.
	string id;
	cout<<"Enter student's ID:";
	cin>>id;

	int index=search(st,id,itemcount);
	if (index != -1) { 								
		cout<<left<<setw(5)<<st[index].stnumber<<setw(20)<<st[index].stname<<setw(5)<<st[index].sex;
		cout<<setw(5)<<st[index].quizz1<<setw(5)<<st[index].quizz2<<setw(5)

		<<st[index].assigment
		<<setw(5)<<st[index].midterm<<setw(5)<<st[index].final<<setw(5)
		<<st[index].total;
		cout<<"\n"; 

	}
	else cout<<"The record doesn't exits.";

}

//!Called when chosen option 9,this arranges the data according to the total score of each student in 
//!increasing order.
/*
	\param dataset[] -> a student array
	\param n -> size of the dataset[] we need to consider.
	\return void
*/
void bubblesort(struct student dataset[], int n){
	int i, j;
	for (i = 0; i < n; i++)
		for (j = n - 1; j > i; j--)
			if (dataset[j].total < dataset[j - 1].total ){
				student temp = dataset[j];
				dataset[j] = dataset[j - 1];
				dataset[j - 1] = temp;
			}

}

//!This is called when option 5 is chosen,where the average marks of the student is displayed.
/*
	\param st[] -> a student array
	\param itemcount -> number of items that we choose to consider from the student array.
	\return void
*/
void average(struct student st[], int itemcount){
	string id;
	float avg=0;
	cout<<"Enter students'ID:";
	cin>>id;
	int index = search(st, id,itemcount);
	if (index != -1 && itemcount>0)
	{
		st[index].total = st[index].quizz1 + st[index].quizz2 + st[index].assigment
			+ st[index].midterm + st[index].final;
		
		avg = st[index].total /5;
	}

	cout<<"The average score is "<<avg;
}

//!The driving function where we can create a student database.
int main(int argc, char *argv[]){
	//!
		//!@param st[80] -> a student array of size 80 (of struct student).
		//!@param itemcount ->no of items (students ) in the database.
	
	student st[80];
	int itemcount=0;
	//!Choose an option from the diplay menu. 
	int yourchoice;
	char confirm;
	do{
	
		displaymenu();
		cout<<"Enter your choice(1-9):";
		cin>>yourchoice;

		switch(yourchoice){
			case 1:add_rec(st, itemcount);break;
			case 2:delete_rec(st, itemcount);break;
			case 3:update_rec(st, itemcount);break;
			case 4:viewall(st, itemcount);break;
			case 5:average(st, itemcount);break;
			case 6:showmax(st, itemcount);break;
			case 7:showmin(st, itemcount);break;
			case 8:find(st, itemcount);break;

			case 9:bubblesort(st,itemcount);break;
			default:cout<<"invalid";
		}

		cout<<"Press y or Y to continue:";
		cin>>confirm;
	}while(confirm=='y'||confirm=='Y');

	system("PAUSE");
	
	return EXIT_SUCCESS;
}