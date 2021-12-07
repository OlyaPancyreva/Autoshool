<template>
  <div id="app">
    <Header></Header>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<style>
#app {
    font-family: 'Roboto Condensed', sans-serif;
    margin-left: auto;
    margin-right: auto;
  }

#my-form {
  margin: 50px;
}

#contact-card {
  width: 1300px;
  margin-top: 50px;
  margin-left: auto;
  margin-right: auto;
  font-size: 20px;
}
</style>
<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default {
  components: {Footer, Header}
}
</script>