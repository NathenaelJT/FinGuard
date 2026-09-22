'use client';
import {useEffect,useState} from "react";
import {getTransactions} from "../../../lib/api";
export default function Transactions(){
 const [rows,setRows]=useState<any[]>([]); const [search,setSearch]=useState(""); const [status,setStatus]=useState("");
 useEffect(()=>{getTransactions(search,status).then(setRows).catch(()=>setRows([]))},[search,status]);
 return <div className="shell"><aside className="side"><div className="brand">Fin<span>Guard</span></div><nav className="nav"><a href="/">Overview</a><a href="/transactions">Transactions</a><a href="/investigations">Investigations</a><a href="/rules">Fraud Rules</a></nav></aside>
 <main className="main"><div className="top"><div><div className="eyebrow">Monitoring</div><h1 className="title">Transactions</h1><div className="muted">Search and triage transaction activity.</div></div></div>
 <div className="card"><div className="toolbar"><input className="input" placeholder="Search reference, customer, country..." value={search} onChange={e=>setSearch(e.target.value)}/><select className="select" value={status} onChange={e=>setStatus(e.target.value)}><option value="">All statuses</option><option>blocked</option><option>review</option><option>monitoring</option></select></div>
 <table className="table"><thead><tr><th>Reference</th><th>Customer</th><th>Amount</th><th>Channel</th><th>Country</th><th>Risk</th><th>Status</th></tr></thead><tbody>{rows.map(x=><tr key={x.id}><td>{x.reference}</td><td>{x.customer}</td><td>{x.currency} {x.amount.toLocaleString()}</td><td>{x.channel}</td><td>{x.country}</td><td className={x.risk_score>=70?"high":""}>{x.risk_score}</td><td><span className="pill">{x.status}</span></td></tr>)}</tbody></table></div></main></div>
}
