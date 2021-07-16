/**
*@file array.cpp
@brief Operations on a 2-Dimentional Array defined over here 
@details 
<pre>
    -Initialising the given 7*7 two-dimenisonal  by filling them with random numbers.
    -Printing out the spiral form of the given array.
    -Printing all the elements of few continuous columns.
    -Finding out the minimum value present in the given array.
    -Finding out the average of all the elements present in the given 2-D array.
</pre>
*/

#include <iostream>
#include <stdlib.h>

using namespace std;

//!This function fills the 7*7 two dimensional array with random elements
/*!
    \param myArr[7][7] an 7*7 two dimesnional array.
    \return void
*/
int fillArray(int myArr[7][7])                 
{
    for(int i=0;i<7;i++)
    {
        for(int j=0;j<7;j++)                    
        {
            myArr[i][j]=20+rand()%400;//!Every element of the two-dimensional array is filled with an element from range [20,419]              
        }
    }
    return 0;
}
//!Printing the elements as we replicate a spiral path in the two dimensional array
/*! 
   \param myArr[7][7]  input 2-D array
   \return void
*/

void printSpiral(int myArr[7][7])
{
    cout << "Array Spiral Function." << endl;
    for(int j=0;j<1;j++)                           
    {                                              
        for(int i=0;i<7;i++)
        {
            cout<< myArr[i][j]<< "  ";//!This prints all the elements in the first column in order
        }

    }
    cout << endl;

    for(int i=6;i<7;i++)                          
    {                                            
        for(int j=1;j<7;j++)
        {
            cout << myArr[i][j] << "  ";//!This prints all the elements in the seventh row in order
        }
    }
    cout << endl;

    for(int j=6;j<7;j++)                          
    {                                             
        for(int i=5;i>=0;i--)
        {
            cout << myArr[i][j] << "  ";//!This prints the first to sixth elements in the seventh column in reverse order
        }
    }
    cout << endl;

    for (int i=0;i<1;i++)                          
    {                                              
        for (int j=5;j>=1;j--)
        {
            cout << myArr[i][j] << "  ";//!This prints the middle five elements in the first row in reverse order
        }
    }
    cout << endl;

    for (int j=1; j<2;j++)
    {                                             
        for (int i=1; i<6;i++)
        {
            cout << myArr[i][j] << "  ";//!This prints the middle five elements in the second column in order
        }
    }
    cout << endl;

    for (int i=5; i<6;i++)                        
    {
        for (int j=2; j<6; j++)
        {
            cout << myArr[i][j] << "  ";//!This prints the elements from third to sixth positions in the sixth row in order
        }
    }
    cout << endl;

    for (int j=5; j<6; j++)                        
    {
        for (int i=4; i>0; i--)
        {
            cout << myArr[i][j] << "  ";//!This prints the elements from second to fifth positions in the sixth column in reverse order
        }
    }
    cout << endl;

    for (int i=1; i<2; i++)                        
    {
       for (int j=4; j>1; j--)
       {
           cout << myArr[i][j] << "  ";//!This prints the elements from third to fifth positions in the second row in reverse order
       }
    }
    cout << endl;

    for (int j=2; j<3; j++)                        
    {
        for (int i=2; i<5; i++)
        {
            cout << myArr[i][j] << "  ";//!This prints the elements from third to fifth positions in the sthird column in order
        }
    }
    cout << endl;

    for (int i=4; i<5; i++)                        
    {
        for (int j=3; j<5; j++)
        {
            cout << myArr[i][j] << "  ";//!This prints the fourth and fifth elements in the fifth row in order
        }
    }
    cout << endl;

    for (int j=4; j<5; j++)                        
    {
        for (int i=3; i>1; i--)
        {
            cout << myArr[i][j] << "  ";//!This prints the third and fourth elements in the fifth column in reverse order
        }
    }
    cout << endl;

    for (int i=2; i<3; i++)                        
    {
        for (int j=3; j<4; j++)
        {
            cout << myArr[i][j] << "  ";//!This prints the fourth element of the third row
        }
    }
    cout << endl;

    for (int i=3; i<4; i++)                         
    {
        for (int j=3; j<4; j++)
        {
            cout << myArr[i][j] << "  ";//!This prints the fourth element of fourth row
        }
    }
  cout << endl << endl;
  //!Finally the printed values are generated  by traversing in a spiral manner. 
}

//!This prints indicated columns of the given two-dimenisonal array of size 7*7
/*!
    \param myArr[7][7]
    \param s -> staring index
    \param e -> final index
    \return void
*/
void printCol(int myArr[7][7], int s, int e)                     
{  
    cout << "Column Output" << endl;                
    for (int j=s-1; j<e-1; j++)
    {                                               
        for (int i=0; i<7; i++)
        {
            cout << myArr[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl << endl;
}

//!Function to find minimum value in the two dimensional array(myArr[7][7])
/*!
    \param myArr[7][7]
    \return smallest element in the array
*/
int findMin (int myArr[7][7])
{
    int i,j;
    int min = myArr[0][0];

    for (i=0; i<7; i++)                             
    {//!Goes through every row of the myarr[7][7]
        for (j=0; j<7; j++)
        {//!Goes through the elements in seven columns in a particular row and if any element in this row is less than
        //!the present min value then the min is changed to this value. 
            if(myArr[i][j] < min)                   
            {                                       
                min = myArr[i][j];
            }                                       
        }                                           

    }
    return min;
}

//!Function to find the average of all the elements present in the array
/*!
    \param myArr[7][7] -> a two dimesional array
    \return the average of all values in the array.
*/
int findAverage (int myArr[7][7])                  
{                                                   
    int i,j;
    int sum = 0;

    for (i=0; i<7; i++)                             
    {
        for (j=0; j<7; j++)
        {
            sum = sum + myArr[i][j];
        }

    }
    return sum/49;       
}
//!To print all the elements in the two dimesional array.
void printArray (int myArr[7][7])                     
{
    cout << "Normal Array Output" << endl;
    //!Prints all the elements in the two dimensional array row wise
    for (int i =0; i<7; i++)
    {
        for (int j=0; j<7; j++)
        {
            cout << myArr[i][j] << "  ";
        }
        cout << endl;
    }
    cout << endl;                                   
    cout << endl;
}
//!The main function to run the program.
int main(){
    
    int myArr [7][7];
    fillArray(myArr);                               
    printArray(myArr);
    printSpiral(myArr);
    printCol(myArr, 2, 5);
    cout<<"Min:"<<findMin(myArr);
    cout<<" Average:"<<findAverage(myArr);
    cout<<endl;

    return 0;
}
 