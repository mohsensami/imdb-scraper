<template>
  <div class="bg-[url('./public/img/bg.jpg')] bg-no-repeat bg-cover">
    <Header />
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";

</script>

<style>

</style>
