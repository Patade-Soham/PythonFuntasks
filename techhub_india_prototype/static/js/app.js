\
document.addEventListener("DOMContentLoaded", () => {
  const open = document.getElementById("openSearch");
  const drawer = document.getElementById("searchDrawer");
  const closeBtn = document.getElementById("closeSearch");
  const input = document.getElementById("searchInput");
  const results = document.getElementById("searchResults");
  function show() { drawer.classList.remove("hidden"); input.focus(); }
  function hide() { drawer.classList.add("hidden"); }
  if(open) open.addEventListener("click", show);
  if(closeBtn) closeBtn.addEventListener("click", hide);
  if(drawer) drawer.addEventListener("click", (e)=>{ if(e.target===drawer) hide(); });
  if(input){
    input.addEventListener("input", async (e) => {
      const q = e.target.value.trim();
      if(!q){ results.innerHTML = ""; return; }
      const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
      const data = await res.json();
      results.innerHTML = data.map(item => `
        <div class="p-3 rounded-lg border">
          <div class="text-xs text-slate-500">${item.category || item.kind || ""}</div>
          <div class="font-semibold">${item.name}</div>
          <div class="text-sm text-slate-600">${item.description || ""}</div>
        </div>
      `).join("");
    });
  }
});
