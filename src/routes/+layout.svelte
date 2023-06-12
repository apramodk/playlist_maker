<script>
    import "../app.css"
    import { page } from '$app/stores';
</script>

<slot/>

<style>
    :global(html) {
        width: 100vw;
        height: 100vh;
    }
</style>