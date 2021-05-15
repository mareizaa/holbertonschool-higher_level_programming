#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: integer
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *aux = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	if (!*head)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	if (number < aux->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (aux)
	{
		if (aux->next == NULL)
		{
			new_node->next = NULL;
			aux->next = new_node;
			return (new_node);
		}
		if (number > aux->n && number <= aux->next->n)
		{
			new_node->next = aux->next;
			aux->next = new_node;
			return (new_node);
		}
		aux = aux->next;
	}
	return (NULL);
}
