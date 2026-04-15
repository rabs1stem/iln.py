const API = "/api";

async function load() {
  const res = await fetch(API + "/reasons");
  const data = await res.json();

  const list = document.getElementById("list");
  list.innerHTML = "";

  data.forEach(item => {
    const li = document.createElement("li");
    li.innerText = item[1];
    list.appendChild(li);
  });
}

async function add() {
  const input = document.getElementById("input");

  await fetch(API + "/reasons", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ text: input.value })
  });

  input.value = "";
  load();
}

load();