#include "main.h"

struct node* addToEmpty(struct node* head, int data)
{
	struct node* temp = malloc(sizeof(struct node));
	
	temp->prev = NULL;
	temp->data = data;
	temp->next = NULL;
	head = temp;

	return (head);
}


struct node* addAtBeg(struct node* head, int data)
{
	struct node* temp = malloc(sizeof(struct node));
	temp->prev = NULL;
	temp->data = data;
	temp->next = NULL;
	temp->next = head;
	head->prev = temp;
	head = temp;

	return (head);
}

struct node* addAtEnd(struct node* head, int data)
{
	struct node *temp, *tp;
	temp = malloc(sizeof(struct node));
	temp->prev = NULL;
	temp->data = data;
	temp->next = NULL;
	tp = head;
	while (tp->next != NULL)
		tp = tp->next;
	tp->next = temp;
	temp->prev = tp;

	return (head);
}

struct node* addAfterPos(struct node* head, int position, int data)
{
	struct node* newP = NULL;
	struct node* temp = head;
	struct node* temp2 = NULL;
	newP = malloc(sizeof(struct node) * sizeof(int));
	newP->prev = NULL;
	newP->data = data;
	newP->next = NULL;

	while (position > (position - 1))
	{
		temp = temp->next;
		position--;
	}
	if (temp->next == NULL)
	{
		temp->next = newP;
		newP->prev = temp;
	}
	else
	{

		temp2 = temp->next;
		temp->next = newP;
		temp2->prev = newP;
		newP->next = temp2;
		newP->prev = temp;
	}

	return (head);
}
