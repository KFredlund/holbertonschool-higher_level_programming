#include "lists.h"
/**
* check_cycle - A function that checks if a singly linked list
* has a cycle in it
* @list: singly linked list
*
* Return: 0 if no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *first_p = list, *second_p = list;

	while (first_p && second_p && second_p && second_p->next)
	{
		first_p = first_p->next;
		second_p = second_p->next->next;
		if (first_p == second_p)
			return (1);
	}
	return (0);
}
