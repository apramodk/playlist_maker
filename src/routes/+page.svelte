<script>
    export let data;
</script>

<div class="h-screen flex items-center justify-center">
    <div class="card w-96 bg-base-100 shadow-xl">
        <form method="POST" class="card-body">
            <h2 class="card-title justify-center">Login</h2>
            <label class="form-control">
                <span class="label label-text">Email</span>
                <input class="input input-bordered" type="email"/>
            </label>

            <label class="form-control">
                <span class="label label-text">Password</span>
                <input class="input input-bordered" type="password"/>
            </label>
            <div class="card-actions justify-center">
                <button class="btn">submit</button>
            </div>
        </form>
    </div>
</div>