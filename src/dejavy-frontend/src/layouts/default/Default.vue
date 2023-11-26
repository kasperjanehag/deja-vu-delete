<template>
  <v-container fluid>
    <v-row no-gutters>
      <SideBarLayout>
        <!-- Sidebar content goes here -->
      </SideBarLayout>
      <MainContainer>
        <!-- Main content goes here -->
      </MainContainer>
    </v-row>
  </v-container>
</template>

<script>
import SideBarLayout from './SideBarLayout.vue'
import MainContainer from './MainLayout.vue'

export default {
  components: {
    SideBarLayout,
    MainContainer
  }
}
</script>

<style scoped>
.v-container {
  background-color: #edf2f7;
}
</style>
