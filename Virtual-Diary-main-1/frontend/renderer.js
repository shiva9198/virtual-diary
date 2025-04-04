document.getElementById("submit").addEventListener("click", async () => {
    const content = document.getElementById("entry").value;
    const hour = new Date().getHours();

    const response = await fetch("http://localhost:5000/add_entry", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ hour, content })
    });

    const data = await response.json();
    alert(data.message);
});