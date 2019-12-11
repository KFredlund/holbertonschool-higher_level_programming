#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
* insert_node - A function that inserts a number
* into a sort singly linked list
* @head: points to beginning
* @number: value in node
*
* Return: Address of new node, or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
	listint_t *current = *head;

	new_node->n = number;
	if (!number)
		return (NULL);
	if (!new_node->next)
		return (NULL);
	new_node->next = NULL;
	if (current->n > current->next->n)
	{
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
