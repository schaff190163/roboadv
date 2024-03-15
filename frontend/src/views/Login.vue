<template>
    <div>
        <h1>Login</h1>
        <form @submit="login">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" required>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login() {
            // Perform login logic here
            // You can access the entered username and password using this.username and this.password
        }
    }
};
</script>

<style scoped>
/* Add your custom styles here */
</style>