import shutil
import frappe
import subprocess
from pathlib import Path


def apply_overrides():
    bench_path = Path(frappe.get_bench_path())

    education_src = (
        bench_path
        / "apps"
        / "education"
        / "frontend"
        / "src"
    )

    custom_src = (
        bench_path
        / "apps"
        / "student_profile"
        / "student_profile"
        / "overrides"
    )

    files_to_copy = [
        (
            custom_src / "Sidebar.vue",
            education_src / "components" / "Sidebar.vue"
        ),
        (
            custom_src / "SidebarLink.vue",
            education_src / "components" / "SidebarLink.vue"
        ),
        (
            custom_src / "StudentDashboard.vue",
            education_src / "pages" / "StudentDashboard.vue"
        ),
        (
            custom_src / "router.js",
            education_src / "router.js"
        ),
    ]

    for source, destination in files_to_copy:
        if not source.exists():
            frappe.log_error(
                f"Missing override file: {source}",
                "Student Profile Override"
            )
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    frappe.logger().info("Education overrides applied")

    build_education_frontend(bench_path)


def build_education_frontend(bench_path):
    frontend_path = (
        bench_path
        / "apps"
        / "education"
        / "frontend"
    )

    try:
        subprocess.run(
            ["npm", "run", "build"],
            cwd=frontend_path,
            check=True
        )

        frappe.logger().info(
            "Education frontend build completed"
        )

    except subprocess.CalledProcessError as e:
        frappe.log_error(
            str(e),
            "Education Frontend Build Failed"
        )
        raise