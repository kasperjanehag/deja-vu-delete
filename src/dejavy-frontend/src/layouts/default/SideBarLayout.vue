<template>
  <v-col cols="3" class="d-flex flex-column overflow-hidden">
    <slot name="logo"></slot>
    <slot name="refresh-button"></slot>
    <v-card flat tile class="flex-grow pa-4 mb-4 mx-4 overflow-auto">
      <slot name="file-tree"></slot>
    </v-card>
  </v-col>
</template>

<style scoped>
.v-col {
  background: white;
  box-shadow: 0px 10px 15px -3px rgba(0, 0, 0, 0.1), 0px 4px 6px -2px rgba(0, 0, 0, 0.05);
  border-radius: 0.5rem;
}
.v-card {
  background: #edf2f7;
  border: 1px solid #d2d6dc;
  border-radius: 0.5rem;
}
</style>