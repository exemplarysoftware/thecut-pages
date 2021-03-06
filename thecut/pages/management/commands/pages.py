# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    args = '[create]'

    def add_arguments(self, parser):
        parser.add_argument('command')

        parser.add_argument('--quantity',
                            action='store',
                            type=int,
                            dest='quantity',
                            default=1,
                            help='Number of instances to create'),

    help = 'create: Create page(s) with fake data'

    def handle(self, *args, **options):

        if 'command' not in options:
            raise CommandError('No command')

        command = options['command']

        if command not in ['create']:
            raise CommandError('"{0}" is not a valid argument'.format(command))

        if command == 'create':
            from ...factories import PageFakerFactory
            quantity = options['quantity']
            PageFakerFactory.create_batch(quantity)

            output = 'Created {0} page(s) with fake data'.format(quantity)
            try:
                self.stdout.write(output)
            except AttributeError:
                print(output)
