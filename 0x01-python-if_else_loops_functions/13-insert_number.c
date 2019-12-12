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
	listint_t *new_node;
	listint_t *current;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
/*	new_node->next = NULL;   */
	current = *head;
	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (*head);
	}
	if (current->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current->next || current)
	{
		if (current->next == NULL)
		{
			current->next = new_node;
			return (new_node);
		}
		if (current->next->n > new_node->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	return (NULL);
}
