const API = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

export async function getOverview() {
  const r = await fetch(`${API}/dashboard/overview`, {cache:"no-store"});
  if (!r.ok) throw new Error("Dashboard request failed");
  return r.json();
}
export async function getTransactions(search="", status="") {
  const p = new URLSearchParams();
  if (search) p.set("search", search);
  if (status) p.set("status", status);
  const r = await fetch(`${API}/transactions?${p}`, {cache:"no-store"});
  if (!r.ok) throw new Error("Transactions request failed");
  return r.json();
}
export async function getInvestigations() {
  const r = await fetch(`${API}/investigations`, {cache:"no-store"});
  if (!r.ok) throw new Error("Investigations request failed");
  return r.json();
}
export async function updateInvestigation(id:number,status:string) {
  const r = await fetch(`${API}/investigations/${id}/status`, {
    method:"PATCH", headers:{"Content-Type":"application/json"},
    body:JSON.stringify({status})
  });
  if (!r.ok) throw new Error("Status update failed");
  return r.json();
}
export async function getRules() {
  const r = await fetch(`${API}/rules`, {cache:"no-store"});
  if (!r.ok) throw new Error("Rules request failed");
  return r.json();
}
export async function toggleRule(id:number) {
  const r = await fetch(`${API}/rules/${id}/toggle`, {method:"PATCH"});
  if (!r.ok) throw new Error("Rule update failed");
  return r.json();
}
