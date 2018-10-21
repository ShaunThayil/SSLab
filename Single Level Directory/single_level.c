#include<stdio.h>
#include<string.h>


typedef struct{
    char name[20];
 }file;

void disp_folder(file st[],int free_list[],int length){ //Display The Contents Of The Directory
    for(int i=0;i<length;i++){
        if(free_list[i]==0){
            printf("%s\n",st[i].name);
        }
    }
}
int search(file st[],char filename[],int length){   //Search For a File In The Directoryand return index if exists else return -1
    int i;
    for(i=0;i<length;i++){
        if(!strcmp(filename,st[i].name)){
            return i;
        }
    }

    return -1;
}

 void initialize(int free_list[],int length){   //Initialize The Free List With 1 i.e Free
     for(int i=0;i<length;i++){
         free_list[i]=1;
     }
 }

void  insert(file st[],int free_list[],int length){   //Insert A File Into The Directory
      int index;
      char new_file[20];
      
      int i;
      
      printf("Enter The Name Of The New File:");
      scanf("%s",new_file);
      printf("\n");

      if(search(st,new_file,length)!=-1){       //Exits If File Already Exists
            printf("File Already Exists!!!\n");
            return;
      }
     
      
      for(i=0;i<length;i++){
          if(free_list[i]==1){
              index=i;
              break;
          }
          
      }
      
      if(i==length){
                  printf("Memory Full\n");
                  return;
              
          }
      
      


      strcpy(st[index].name,new_file);
      free_list[index]=0;

}


void   delete(file st[],int free_list[],int length){     //Delete a File From The Directory
    char filename[20];
    int index;

    printf("Enter The Name Of The File You Want To Delete: ");
    scanf("%s",filename);

    index=search(st,filename,length);
    if(index==-1){
        printf("File Does Not Exist!!\n");
        return;
    }
    free_list[index]=1;
    

}



void main(){
    file st[20];
    int option,length=20;
    int free_list[20];
    char file_name[20];
    int index;
    initialize(free_list,length);
    while(1){
       printf("Choose The Operation You Want To Perform:-\n");
       printf("1>Insert A File\n2>Delete A File\n3>Search For  A File\n4>Display\n5>Exit\n");
       printf("Operation:");
       scanf("%d",&option);
    
       if(option==1){
           insert(st,free_list,length);
       }
       else if(option==2){
            delete(st,free_list,length);
       }
       else if(option==3){
           printf("Enter FileName:\n");
           scanf("%s",file_name);
           index=search(st,file_name,length);
           if(index==-1){
               printf("File Does Not Exist!!\n");
           }
           else{
               printf("File Exists At Index %d",index);
           }
       }
        else if(option==4){
            disp_folder(st,free_list,length);
        }

        else if(option==5){
            break;
        }
        printf("\n");
    }
}