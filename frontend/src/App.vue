<template>
  <div id="app">
    <div class="uk-background-secondary">
      <div class="padlr padtop uk-position-top-center">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<style>
.padlr {
  padding-left: calc(15px + 1vw);
  padding-right: calc(15px + 1vw);
}
.padtop {
  padding-top: calc(15px + 4vh);
}
h1 {
  background: linear-gradient(to bottom, #0000 65%, #5c97da 50%);
}
h1, h2, h3, h4, h5, h6, p {
  color: #333 !important;
}
html {
  background-color: #fcfcfc !important;
}
</style>
