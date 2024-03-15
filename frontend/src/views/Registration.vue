<template></template>
    <div>
        <h1>User Registration</h1>
        <form @submit.prevent="registerUser">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required>
            <br>
            <button type="submit">Register</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            email: '',
            password: ''
        };
    },
    methods: {
        registerUser() {
            // Perform user registration logic here
            // You can use this.username, this.email, and this.password to access the form values
        }
    }
};
</script>

<style scoped>
/* Add your custom styles here */
</style>