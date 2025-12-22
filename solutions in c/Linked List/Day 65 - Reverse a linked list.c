//We use two pointers to keep track of current node and next node.
//Using the pointers we reverse the direction of link.
//temp is used to traverse the list starting at head.

struct Node* reverseList(struct Node* head) {
    struct Node* temp=head,*prev=NULL,*next; 
  
    while(temp!=NULL){      //Example:  n->m->o->p
        next=temp->next;    //temp=n; prev=NULL;
        temp->next=prev;    //next=m; n->link=NULL; prev=n; temp=m;      NULL<-n m->o->p
        prev=temp;          //next=o; m->link=n; prev=m; temp=o;         NULL<-n<-m o->p
        temp=next;          //next=p; o->link=m; prev=o; temp=p;         NULL<-n<-m<-o p
    }                       //next=NULL; p->link=o; prev=p; temp=NULL;   NULL<-n<-m<-o<-p
                            //head=prev i.e,head=p;
    head=prev;
    return head;
}
