'use client';
import {useEffect,useState} from "react";
import {getRules,toggleRule} from "../../../lib/api";
export default function Rules(){
 const [rows,setRows]=useState<any[]>([]);
 const load=()=>getRules().then(setRows).catch(()=>setRows([]));
 useEffect(load,[]);
 async function toggle(id:number){await toggleRule(id);load()}
 return <div className="shell"><aside className="side"><div className="brand">Fin<span>Guard</span></div><nav className="nav"><a href="/">Overview</a><a href="/transactions">Transactions</a><a href="/investigations">Investigations</a><a href="/rules">Fraud Rules</a></nav></aside>
 <main className="main"><div className="top"><div><div className="eyebrow">Detection controls</div><h1 className="title">Fraud Rules</h1><div className="muted">Manage thresholds and detection policies.</div></div></div>
 <div className="card"><table className="table"><thead><tr><th>Rule</th><th>Description</th><th>Threshold</th><th>Severity</th><th>Enabled</th></tr></thead><tbody>{rows.map(x=><tr key={x.id}><td><b>{x.name}</b></td><td>{x.description}</td><td>{x.threshold}</td><td><span className="pill">{x.severity}</span></td><td><button className="button" onClick={()=>toggle(x.id)}>{x.enabled?"Disable":"Enable"}</button></td></tr>)}</tbody></table></div></main></div>
}
