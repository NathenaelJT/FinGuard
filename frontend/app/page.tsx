'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';

type Overview = {
  total_transactions: number;
  high_risk: number;
  volume: number;
  open_cases: number;
  active_rules: number;
};

const emptyOverview: Overview = {
  total_transactions: 0,
  high_risk: 0,
  volume: 0,
  open_cases: 0,
  active_rules: 0,
};

export default function Home() {
  const [data, setData] = useState<Overview>(emptyOverview);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/dashboard/overview')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to load dashboard');
        }
        return response.json();
      })
      .then((result) => {
        setData(result);
      })
      .catch((error) => {
        console.error('Dashboard error:', error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="shell">
      <aside className="side">
        <div className="brand">
          Fin<span>Guard</span>
        </div>

        <nav className="nav">
          <Link href="/">Overview</Link>
          <Link href="/transactions">Transactions</Link>
          <Link href="/investigations">Investigations</Link>
          <Link href="/rules">Fraud Rules</Link>
        </nav>
      </aside>

      <main className="main">
        <div className="top">
          <div>
            <div className="eyebrow">Financial operations</div>
            <h1 className="title">Risk Command Center</h1>
            <div className="muted">
              Monitor transaction exposure and investigation workload.
            </div>
          </div>
        </div>

        <div className="grid">
          <Metric
            title="Transactions"
            value={loading ? '—' : data.total_transactions}
          />

          <Metric
            title="High Risk"
            value={loading ? '—' : data.high_risk}
            danger
          />

          <Metric
            title="Transaction Volume"
            value={
              loading
                ? '—'
                : `ETB ${Number(data.volume).toLocaleString()}`
            }
          />

          <Metric
            title="Open Cases"
            value={loading ? '—' : data.open_cases}
          />
        </div>

        <div className="section card">
          <div className="kicker">Operational snapshot</div>

          <p className="muted">
            Active fraud rules:{' '}
            <b>{loading ? '—' : data.active_rules}</b>
          </p>

          <p className="muted">
            Use the navigation to investigate high-risk activity and
            manage detection controls.
          </p>
        </div>
      </main>
    </div>
  );
}

function Metric({
  title,
  value,
  danger = false,
}: {
  title: string;
  value: string | number;
  danger?: boolean;
}) {
  return (
    <div className="card">
      <div className="muted">{title}</div>

      <div className={`metric ${danger ? 'danger' : ''}`}>
        {value}
      </div>
    </div>
  );
}