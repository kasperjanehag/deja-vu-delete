<template>
    <v-card
      class="mx-auto"
    >
      <v-list>
        
        <NestedListItems :items="items"></NestedListItems>
  
      </v-list>
    </v-card>
  </template>
  
<script>

import NestedListItems from './NestedListItems.vue';

export default {
    components: {
        NestedListItems
    },
    data: function() {
        return {
            items: [
                {
                    id: 1,
                    name: 'File 1',
                    icon: 'mdi-account',
                },
                {
                    id: 2,
                    name: 'Folder 1',
                    icon: 'mdi-plus-outline',
                    isOpen: false,
                    children: [
                        {
                            id: 3,
                            name: 'File 2',
                            icon: 'mdi-account-multiple-outline',
                        },
                        {
                            id: 4,
                            name: 'File 3',
                            icon: 'mdi-cog-outline',
                        },

                        {
                            id: 5,
                            name: 'Sub Folder 1',
                            icon: 'mdi-plus-outline',
                            isOpen: false,
                            children: [
                                {
                                    id: 6,
                                    name: 'File 2',
                                    icon: 'mdi-account-multiple-outline',
                                },
                                {
                                    id: 7,
                                    name: 'File 3',
                                    icon: 'mdi-cog-outline',
                                },
                            ],
                        },
                        {
                            id: 8,
                            name: 'Sub Folder 2',
                            isOpen: false,
                            icon: 'mdi-database',
                            children: [
                                { id: 9, name: 'Create', icon: 'mdi-plus-outline' },
                                { id: 10, name: 'Read', icon: 'mdi-file-outline' },
                                { id: 11, name: 'Update', icon: 'mdi-update' },
                                { id: 12, name: 'Delete', icon: 'mdi-delete' },
                            ],
                        },
                    ],
                },
                {
                    id: 4,
                    name: 'Folder 2',
                    isOpen: false,
                    icon: 'mdi-database',
                    children: [
                        { id: 5, name: 'Create', icon: 'mdi-plus-outline' },
                        { id: 6, name: 'Read', icon: 'mdi-file-outline' },
                        { id: 7, name: 'Update', icon: 'mdi-update' },
                        { id: 8, name: 'Delete', icon: 'mdi-delete' },
                    ],
                },
            ],
        }
    }
}
</script>
