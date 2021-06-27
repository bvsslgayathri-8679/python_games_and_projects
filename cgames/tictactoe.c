 #include <stdlib.h>
 #include<stdio.h>
 #include<conio.h>
 #include<string.h>
  int main()
  {
  z: {char square[10]={'0','1','2','3','4','5','6','7','8','9'};
     int choice ,player;
  
       int i=0,count=1,a,j;
       int returnvalue=0;
       char mark,p1[10],p2[10],s[10],x[10];
       player=1;
       gotoxy(9,7);
       printf("??TIC TAC TOE??");
       gotoxy(10,10);
       printf("0.?START?");
       gotoxy(10,12);
       printf("1.??HELP??");
       gotoxy(10,14);
       printf("2.??EXIT??");
       gotoxy(30,25);
       scanf("%d",&a);
       clrscr();
switch(a)
{
    case 0:{
              printf("Enter player names:\n");
              scanf("%s%s",p1,p2);
              clrscr();
              gotoxy(4,2);
              printf("%s(x) - %s(0)",p1,p2);
              x:do
              {
                    gotoxy(8,1);
                    printf("??TIC TAC TOE??");
                    gotoxy(10,4);
                    printf("   |   |   ");
                    gotoxy(10,5); 
                    printf(" %c | %c | %c",square[1],square[2],square[3]);
                    gotoxy(10,6);
                    printf("___|___|___");
                    gotoxy(10,7);
                    printf("   |   |   ");
                    gotoxy(10,8);
                    printf(" %c | %c | %c",square[4],square[5],square[6]);
                    gotoxy(10,9);
                    printf("___|___|___");
                    gotoxy(10,10);
                    printf("   |   |   ");
                    gotoxy(10,11);
                    printf(" %c | %c | %c",square[7],square[8],square[9]);
                    gotoxy(10,12);
                    printf("   |   |   ");
    
                    player=(player%2!=0)?1:2;
                    gotoxy(4,15);
                    printf("??%s enter a number?? ",(player==1)?p1:p2);
                    scanf("%d",&choice);
                    mark = (player==1)?'X':'O';
                  
                  if (choice==1&&square[1]=='1')
                  square[1]=mark; 
                  else if (choice==2&&square[2]=='2')
                  square[2]=mark;
                  else if (choice==3&&square[3]=='3')
                  square[3]=mark;
                  else if (choice==4&&square[4]=='4')
                  square[4]=mark;
                  else if (choice==5&&square[5]=='5')
                  square[5]=mark;
                  else if (choice==6&&square[6]=='6')
                  square[6]=mark;
                  else if (choice==7&&square[7]=='7')
                  square[7]=mark;
                  else if (choice==8&&square[8]=='8')
                  square[8]=mark;
                  else if (choice==9&&square[9]=='9')
                  square[9]=mark;
                
                  else
                   {
                          clrscr();
                          gotoxy(4,18);
                          printf("??last warning?? \n   re-enter the value");
                          goto x;
                   }
                
                clrscr();  
                if(square[1]==square[2]&&square[2]==square[3])
                returnvalue=1;
                else if(square[4]==square[5]&&square[5]==square[6])
                returnvalue=1;
                else if(square[7]==square[8]&&square[8]==square[9])
                returnvalue=1;
                else if(square[1]==square[4]&&square[4]==square[7])
                returnvalue=1;
                else if(square[2]==square[5]&&square[5]==square[8])
                returnvalue=1;
                else if(square[3]==square[6]&&square[6]==square[9])
                returnvalue=1;
                else if(square[1]==square[5]&&square[5]==square[9])
                returnvalue=1;
                else if(square[3]==square[5]&&square[5]==square[7])
                returnvalue=1;
                else if(count==9)
                returnvalue=0;
                else
                returnvalue=2;
    
               count++;
               i=returnvalue;
               player++;
          }while(i==2);
   
          gotoxy(9,1);
          printf("?TIC TAC TOE?");
          gotoxy(10,4);
          printf("   |   |   ");
          gotoxy(10,5);
          printf(" %c | %c | %c",square[1],square[2],square[3]);
          gotoxy(10,6);
          printf("___|___|___");
          gotoxy(10,7);
          printf("   |   |   ");
          gotoxy(10,8);
          printf(" %c | %c | %c",square[4],square[5],square[6]);
          gotoxy(10,9);
          printf("___|___|___");
          gotoxy(10,10);
          printf("   |   |   ");
          gotoxy(10,11);
          printf(" %c | %c | %c",square[7],square[8],square[9]);
          gotoxy(10,12);
          printf("   |   |   ");
  
          if(i==1)
          {
                 gotoxy(8,16);
                 printf("??%s winner??",(--player==1)?p1:p2);
                 if(i!=2)
                 {
                         gotoxy(8,18);
                         printf("??%s looser??",(++player==2)?p2:p1);
                  }
          }
         else
         {
                   gotoxy(8,16);
                   printf("??game is draw??");
         }
          do
          {
                  printf("\nEnter 1 to goto home:");
                  scanf("%s",x);
                  clrscr();
                  goto z;
          }while(x =='y');
       }break;
       
case 1:{
              clrscr();
              gotoxy(12,2);
              printf("??HELP!!??\n\n");
              printf("\n1.the game is played in 3×3 squares which consists of 1 to 9 numbers.\n ");   
              printf("\n2.if any person types the letters grater than 9 or the no is repeated warnings are shown.\n");
              printf("\n3.if warnings are more than 2 the opponent is the winnes");
              gotoxy(15,30);
              printf("press 0 for Back");
              scanf("%d",&j);
              
              if(j==0)
              {
                   clrscr();
                   goto z;
              }
        }break;
        
case 2:{
              clrscr();
              gotoxy(10,15);
              printf("??THANK YOU??\n\n\n\n\n\n");           
       }break;
       
default:{
              gotoxy(10,15);
              printf("\n\nINVALID OPTION!!\nRE-ENTER");
              goto z;
        }
     }
   }
 }

