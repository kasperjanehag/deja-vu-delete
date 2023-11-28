<template>
  <MainLayout>
    <template #logo>
      <v-img src="@/assets/logo.png" alt="Logo" />
    </template>
    <template #refresh-button>
      <v-img src="@/assets/logo.png" alt="Logo" />
    </template>
    <template #file-tree>
      <v-card flat color="grey lighten-2" class="fill-height"></v-card>  <!-- Will be replaced with FileTree -->
    </template>
    <template #title>
      <v-card-title>Dejavy</v-card-title>
    </template>
    <template #image-display>
      <v-img src="@/assets/logo.png" alt="Image Display" />
    </template>
    <template #find-duplicates-button>
      <v-btn color="secondary">Find Duplicates</v-btn>
    </template>
    <router-view />
  </MainLayout>
</template>


<script setup>
import MainLayout from '@/layouts/default/Default.vue'
import { ref } from 'vue'

const items = ref([
  {
    id: 1,
    name: 'Root',
    children: [
      { id: 2, name: 'Child' },
      { id: 3, name: 'Another Child' }
    ]
  }
])
</script>