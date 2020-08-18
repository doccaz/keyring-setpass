/*
 * keyring-setpass
 * Funções deste utilitário:
 * - Remove o keyring de login
 * - Criar um novo keyring default
 * - Define a senha como vazia
 * 
 * Autor: Erico Mendonca <erico.mendonca@suse.com>
 * Mar/2020
 */

#include <gnome-keyring-1/gnome-keyring.h>
#include <glib.h>
#include <stdio.h>

int main()
{

	if (gnome_keyring_is_available())
	{
		fprintf(stdout, "GNOME Keyring disponivel\n");
		fprintf(stdout, "Apagando keyring 'login': %d\n", gnome_keyring_delete_sync("login"));
		fprintf(stdout, "Criando novo keyring 'login': %d\n", gnome_keyring_create_sync("login", ""));
	} else {
		fprintf(stdout, "GNOME keyring não está disponível!\n");
		return 1;
	}

	return 0;

}
