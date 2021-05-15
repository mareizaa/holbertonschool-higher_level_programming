#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *@list: head linked list
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list, *tmpd = list;
	
	while(aux && tmpd && tmpd->next)
	{
		tmpd = tmpd->next->next;
		aux = aux->next;
		if(aux == tmpd)
			return (1);
	}
	return (0);
}
