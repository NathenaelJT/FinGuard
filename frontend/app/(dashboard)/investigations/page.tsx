'use client';
import {useEffect,useState} from "react";
import {getInvestigations,updateInvestigation} from "../../../lib/api";
export default function Investigations(){
 const [rows,setRows]=useState<any[]>([]);
 const load=()=>getInvestigations().then(setRows).catch(()=>setRows([]));
 useEffect(load,[]);
 async function change(id:number,status:string){await updateInvestigation(id,status);load()}
 return <div className="shell"><aside className="side"><div className="brand">Fin<span>Guard</span></div><nav className="nav"><a href="/">Overview</a><a href="/transactions">Transactions</a><a href="/investigations">Investigations</a><a href="/rules">Fraud Rules</a></nav></aside>
 <main className="main"><div className="top"><div><div className="eyebrow">Case management</div><h1 className="title">Investigations</h1><div className="muted">Work suspicious activity through a controlled lifecycle.</div></div></div>
 <div className="card"><table className="table"><thead><tr><th>Case</th><th>Priority</th><th>Owner</th><th>Status</th><th>Action</th></tr></thead><tbody>{rows.map(x=><tr key={x.id}><td><b>{x.title}</b><br/><span className="muted">{x.notes}</span></td><td><span className="pill">{x.priority}</span></td><td>{x.owner}</td><td>{x.status}</td><td><select className="select" value={x.status} onChange={e=>change(x.id,e.target.value)}><option>open</option><option>review</option><option>escalated</option><option>resolved</option><option>dismissed</option></select></td></tr>)}</tbody></table></div></main></div>
}
