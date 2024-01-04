#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list
 * Return: a integer.
 */
int check_cycle(listint_t *list)
{
	listint_t *lts = list;
	listint_t *aux = lts;

	while (lts && aux && lts->next)
	{
		aux = aux->next;
		lts = lts->next->next;
		if (aux == lts)
			return (1);
	}
	return (0);
}
