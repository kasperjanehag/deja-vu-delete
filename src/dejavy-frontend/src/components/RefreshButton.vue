<template>
  <button @click="$emit('refresh')" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4 mx-4">
    Refresh File List
  </button>
</template>

<script>
export default {
  methods: {
    refresh() {
      this.$emit('refresh');
    }
  }
}
</script>