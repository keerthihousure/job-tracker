# 🎯 Job Search Tracker Dashboard
### A Python & Plotly Dash project — because even a job hunt deserves good data

---

## 👋 Why I Built This

Job searching in your final semester of grad school is... a lot.

Between classes, assignments, and sending out applications, I kept losing track of where I stood.
Which companies had I heard back from? Which ones ghosted me? How many interviews had I actually landed?

I was already spending time in Python every day for coursework — so I thought:
*why not just build something that tracks all of this for me?*

That's how this dashboard was born. It started as a personal productivity tool and ended up
becoming one of the projects I'm most proud of — because it combines real data (my actual
job search) with the analytics skills I've been building throughout my MS in Information Systems.

---

## 📊 What the Dashboard Shows

**50 real applications** I sent between **December 2025 and February 2026**, visualised across:

| Metric | Value |
|---|---|
| Total Applications | 50 |
| Active / Pending | 14 |
| Interviews Secured | 10 |
| Offers Received | 2 |
| Rejections | 24 |
| Offer Rate | 4.0% |
| Avg Offer Salary | $123,500 |

The early weeks were rough — a lot of rejections from consulting and big tech.
But the data told a clear story: **FinTech and Analytics companies responded better**,
interviews started picking up in January, and by February I had two offers on the table.

That's the kind of insight you only see when you stop guessing and start tracking.

---

## 🛠️ Tech Stack

| Tool | What I used it for |
|---|---|
| **Python 3.13** | Core language |
| **Pandas** | Data manipulation & KPI calculations |
| **Plotly Express** | Interactive charts (donut, bar, line, box plot) |
| **Plotly Dash** | Web dashboard framework |
| **Dash DataTable** | Filterable, sortable applications table |
| **PyCharm Community** | Development environment |

No cloud services. No paid tools. Just Python and an afternoon of building.

---

## 📈 Charts & Features

- **5 KPI Cards** — total, active, interviews, offers, rejections — all live from the data
- **Status Donut Chart** — visual breakdown of where every application stands
- **Industry Bar Chart** — which sectors I targeted most
- **Weekly Trend Line** — application volume over 12 weeks (you can literally see my momentum build)
- **Salary Box Plot** — how salary ranges compare across Applied → Interview → Offer stages
- **Interactive Table** — filter by status, sort by any column, search by company

---

## 🔍 What the Data Revealed

A few things I only realised *after* seeing the data:

- **FinTech had my best interview rate** — I should have targeted it earlier
- **Big tech rejections came fast** (Google, Meta, Amazon) — useful to know for calibrating expectations
- **Remote roles got faster responses** than onsite ones on average
- **Consistency mattered more than volume** — my best weeks weren't the ones with the most applications,
  they were the ones with the most *targeted* applications

---

## 🗂️ Project Structure

```
job-tracker/
│
├── app.py          ← Full Dash dashboard (layout, charts, callbacks)
├── data.py         ← All 50 job applications as a Python list
└── README.md       ← You're reading it
```

---

## 🚀 Run It Yourself

```bash
# 1. Clone the repo
git clone https://github.com/keerthihousure/job-tracker.git
cd job-tracker

# 2. Install dependencies
pip install dash plotly pandas

# 3. Launch
python app.py

# 4. Open in your browser
# → http://127.0.0.1:8050
```

Want to use it for your own job search? Open `data.py`, replace the sample entries
with your own applications, save, and refresh. That's it.

---

## 💡 What I Learned

Beyond the technical side, this project changed how I approached the job hunt itself.

Seeing rejection rates laid out visually stopped them from feeling personal.
It became a numbers game I could actually optimise — which industries to prioritise,
which application types had the best ROI, when to follow up.

Data doesn't lie. And sometimes the most useful dataset is the one you generate yourself.

---

## 🔗 Related Projects

- 📦 [Vendor Performance Analysis](https://github.com/keerthihousure/Vendor-Performance-Analysis) —
  end-to-end BI project using Python, Power BI & DAX on retail transactional data

---

## 📬 About Me

**Keerthi Housure Srinivas**
Final Semester — MS Information Systems

I turn messy data into decisions that stick.
Open to **Data Analyst** and **Business Intelligence** roles.

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-navy)](https://keerthihousure.github.io/keerthi-hs.github.io)
[![GitHub](https://img.shields.io/badge/GitHub-keerthihousure-black)](https://github.com/keerthihousure)
