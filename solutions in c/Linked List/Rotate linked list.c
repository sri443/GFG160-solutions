#include <stdio.h>
#include <stdlib.h>

// Define the Node structure
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to rotate the linked list to the left by k positions
struct Node* rotateLeft(struct Node* head, int k) {
    int len = 1;
    struct Node* temp = head;
    while (temp->next) {
        len++;
        temp = temp->next;
    }
    
    // Handle k >= len by taking modulo
    k %= len;
    if (k == 0) return head;
    
    // Find the (k-1)th node
    struct Node* curr = head;
    for (int i = 1; i < k; i++) {
        curr = curr->next;
    }
    
    // curr is now the (k-1)th node
    struct Node* new_head = curr->next;
    curr->next = NULL;
    
    // Connect the end of the list to the original head
    temp->next = head;
    return new_head;
}

// Function to print the linked list
void printList(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

// Example usage
int main() {
    // Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    struct Node* head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(4);
    head->next->next->next->next = createNode(5);
    
    printf("Original list: ");
    printList(head);
    
    int k = 2;
    head = rotateLeft(head, k);
    
    printf("After rotating left by %d: ", k);
    printList(head);
    
    // Free memory (not shown for brevity)
    return 0;
}
