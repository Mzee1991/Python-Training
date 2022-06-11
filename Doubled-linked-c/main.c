#include "main.h"

int main(void)
{
	struct node* head = NULL;
	struct node* ptr;
	int position = 2;
	head = addToEmpty(head, 45);
	head = addAtBeg(head, 34);
	head = addAtEnd(head, 9);
	head = addAfterPos(head, position, 100);

	ptr = head;
	while (ptr != NULL)
	{
		printf("%d ", ptr->data);
		ptr = ptr->next;
	}
	printf("\n");

	return (0);
}
