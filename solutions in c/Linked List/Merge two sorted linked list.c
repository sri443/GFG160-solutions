struct Node* sortedMerge(struct Node* head1, struct Node* head2) {
    struct Node* dummy=(struct Node*)malloc(sizeof(struct Node));
    dummy->data=0;
    dummy->next=NULL;
    
    struct Node* curr=dummy;
    
    while(head1!=NULL && head2!=NULL){
        if(head1->data < head2->data){
            curr->next=head1;
            head1=head1->next;
        }
        else{
            curr->next=head2;
            head2=head2->next;
        }
        curr=curr->next;
    }
    
    if(head1!=NULL){
        curr->next=head1;
    }else if(head2!=NULL){
        curr->next=head2;
    }
    
    return dummy->next;
}
