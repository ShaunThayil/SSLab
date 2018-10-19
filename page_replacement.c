#include<stdio.h>

void display(int n){
    printf("There Are :-%d Page Faults\n",n);
}
void disp(int a[],int length){
    for(int i=0;i<length;i++){
        printf("%d ",a[i]);
    }
    printf("\n");
}


int search(int page,int frames[],int framelen){
     int a=-1;
     for(int i=0;i<framelen;i++){
         if(frames[i]==page){
             a=i;
             break;
         }
     }
     return a;
}

void initialize(int frames[],int framelen){
    for(int i=0;i<framelen;i++){
        frames[i]=-1;
    }
}

void initialize_max(int frames[],int framelen){
    for(int i=0;i<framelen;i++){
        frames[i]=10;
    }
}
int min(int least[],int framelen,int lastChanged){
    int m=0;
    for(int i=1;i<framelen;i++){
        if(least[i]<least[m] && i!=lastChanged){
            m=i;
        }
    }

    return m;
}
int max(int least[],int framelen){
      int m=0;
      for(int i=1;i<framelen;i++){
          if(least[i]>least[m]){
                m=i;
          }
      }
   
      return m;

}
void increment_except_index(int least[],int framelen,int index){

   for(int i=0;i<framelen;i++){
       if(i==index){
           least[i]=0;
           continue;
       }
       least[i]++;
   }

}


void fifo(int ref[],int reflength,int framelen){
    int fault=0;
    int frames[framelen];
    int index=0;
    
    initialize(frames,framelen);

    for(int i=0;i<reflength;i++){
        if(search(ref[i],frames,framelen)==-1){
            fault++;
            frames[index]=ref[i];

            index=(index+1)%framelen;
        }
    }

    display(fault);

}

//In This Code You Maintain An Array From Which We Can Find The Least Recently Used Page
void lru(int ref[],int reflength,int framelen){
    int fault=0,index;

    int frames[framelen];
    initialize(frames,framelen);

    int least[framelen];
    initialize_max(least,framelen);


    for(int i=0;i<reflength;i++){
        index=search(ref[i],frames,framelen);
        //printf("%d\n",index);
        if(index==-1){
            index=max(least,framelen);
            frames[index]=ref[i];
            increment_except_index(least,framelen,index);
            fault++;
        }
        else{
            increment_except_index(least,framelen,index);
             
        }

    //disp(frames,framelen);
    }

     
    display(fault);

}


//In LFU you cannout swap out the last changed frame
//In this code you maintain an array for saving the frequency count of each respective page
void lfu(int ref[],int reflength,int framelen){
    int fault=0;
    int frames[framelen];
    int lastChanged=-1;
    initialize(frames,framelen);

    int least[framelen],index;
    initialize(least,framelen);

    for(int i=0;i<reflength;i++){
        index=search(ref[i],frames,framelen);
        if(index==-1){
             index=min(least,framelen,lastChanged);
            // printf("%d\n",index);
             frames[index]=ref[i];
             least[index]=1;
             fault++;
        }
        else{
            least[index]++;
        }
        lastChanged=index;
       // disp(frames,framelen);
    }

    display(fault);

}




void main(){
int framelen,reflength,ref[reflength],option;
printf("Enter The Number OF Frames Available:-\n");
scanf("%d",&framelen);
printf("Enter The Length Of Reference String:-\n");
scanf("%d",&reflength);
printf("Enter The Reference String\n");
for(int i=0;i<reflength;i++){
  scanf("%d",&ref[i]);
}

printf("Choose The Type Of Page Replacement Followed:-\n1> FIFO\n2> LRU\n3> LFU\n");
scanf("%d",&option);

if(option==1){
    fifo(ref,reflength,framelen);
}

else if(option==2){
    lru(ref,reflength,framelen);
}

else{
    lfu(ref,reflength,framelen);
}
}


/*
Sample Inputs And Respective Outputs
FIFO:
3
12
1 2 3 4 1 2 5 1 2 3 4 5
1
OUTPUT:     9

Belady's Anomaly
4
12
1 2 3 4 1 2 5 1 2 3 4 5
1
OUTPUT:     10


LRU:
4
14
1 2 3 4 3 1 4 2 5 2 1 2 3 4
2
OUTPUT:     7

LFU:
3
10
2 3 4 2 1 3 7 5 4 3
3
OUTPUT:     9

*/

