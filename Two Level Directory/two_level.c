#include<stdio.h>
#include<string.h>

typedef struct{
char name[20];

}file;

typedef struct {
char dirname[20];
file f[20];
int free_list[20];
}directory;

void initialize(directory dir[],int free_dir[],int dir_len,int num_file){
         int i,j;
         for(i=0;i<dir_len;i++){
             free_dir[i]=1;
             for(j=0;j<num_file;j++){
                 dir[i].free_list[j]=1;
             }
         }

}


int search_directory(directory dir[],char dirname[],int dir_len){
    for(int i=0;i<dir_len;i++){
        if(strcmp(dir[i].dirname)==0){
            return i;
        }
    }
    
    return -1;
}

int search_file(directory dir,char filename[],int num_file){
    for(int i=0;i<num_file;i++){
        if(strcmp(dir.f[i].name,filename)==0){
            return i
        }
    }

    return -1;
}

void insert_user(directory dir[],int free_dir[],int dir_len){
     char username[20];
     int index=-1;
     printf("Enter UserName: ");
     scanf("%s",username);
      
      if(search(dir,username,dir_len)==-1){
          printf("Directory Already Exists!!");
          return;
      }
     
     for(int i=0;i<dir_len;i++){
         if(free_dir[i]==1){
             index=i;
         }
     }
   
     if(index==-1){
         printf("Directories Full!!\n");
         return;
     }
     strcpy(dir[i].dirname,username);
     free_dir[i]=0;


}


void insert_file(directory dir,int num_file){
    char filename;
    int index=-1;
    printf("Enter Filename: ");
    scanf("%s",filename);
    
    if(search_file(dir,filename,num_file)==-1){
        printf("File Already Exists!!\n");
        return;
    }

    for(int i=0;i<num_file;i++){
        if(dir.free_list[i]==1){
             index=i;
             break;
        }
    }

    if(index==-1){
        printf("Memory Full!!\n");
        return;
    }
    
    strcpy(dir.f[index].name,filename);
    dir.free_list[i]=0;

}



void main(){
    directory dir[10];
    int dir_len=10;
    int num_file=20;
    int n,free_dir[];
    
    initialize(dir,free_dir,dir_len,num_file);

    while(1){
      



       printf("Operations Are:\n");
       printf("1>Create A New User Directory\n2>Change Directory\n3>List All User Directories\n4>Create A File\n5>Delete A file\n6>Search Directory\n7>List Files In Directory\n6>Exit");
       print("Enter Option");
       scanf("%d",&n);

       if(n==1){
           user()
       }

       else if(n==2){

       }

       else if (n==3){

       }

       else if(n==4){

       }

       else if(n==5){

       }

       else if(n==6){
           break;
       }

    }

}