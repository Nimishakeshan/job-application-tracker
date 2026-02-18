const API_URL = "http://127.0.0.1:8000";

const table = document.getElementById("jobTable");
const form = document.getElementById("jobForm");
const company = document.getElementById("company");
const role = document.getElementById("role");
const status = document.getElementById("status");

async function fetchJobs() {
    const res = await fetch(`${API_URL}/jobs`);
    const jobs = await res.json();
    table.innerHTML = "";

    jobs.forEach(job => {
        table.innerHTML += `
        <tr>
            <td>${job.company}</td>
            <td>${job.role}</td>
            <td>
                <select id="status-${job.id}">
                    <option value="Applied" ${job.status === "Applied" ? "selected" : ""}>Applied</option>
                    <option value="Interview" ${job.status === "Interview" ? "selected" : ""}>Interview</option>
                    <option value="Offer" ${job.status === "Offer" ? "selected" : ""}>Offer</option>
                    <option value="Rejected" ${job.status === "Rejected" ? "selected" : ""}>Rejected</option>
                </select>
            </td>
            <td>
                <button class="update" onclick="updateJob(${job.id})">Update</button>
                <button class="delete" onclick="deleteJob(${job.id})">Delete</button>
            </td>
        </tr>`;
    });
}

// Add new job
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const job = {
        company: company.value,
        role: role.value,
        status: status.value
    };

    await fetch(`${API_URL}/jobs`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(job)
    });

    form.reset();
    fetchJobs();
});

// Delete job
async function deleteJob(id) {
    await fetch(`${API_URL}/jobs/${id}`, { method: "DELETE" });
    fetchJobs();
}

// Update job status
async function updateJob(id) {
    const newStatus = document.getElementById(`status-${id}`).value;
    await fetch(`${API_URL}/jobs/${id}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ status: newStatus })
    });
    fetchJobs();
}

// Initial fetch
fetchJobs();
