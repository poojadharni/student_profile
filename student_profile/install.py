import shutil
import subprocess
from pathlib import Path

import frappe
from frappe.utils import get_bench_path


def apply_overrides():
    """
    Copy custom Vue files into Education frontend
    and build Education frontend automatically.
    """

    bench_path = Path(get_bench_path())

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

    # Validate paths
    if not education_src.exists():
        frappe.throw(
            f"Education frontend not found:\n{education_src}"
        )

    if not custom_src.exists():
        frappe.throw(
            f"Overrides folder not found:\n{custom_src}"
        )

    files_to_copy = [
        (
            custom_src / "Sidebar.vue",
            education_src / "components" / "Sidebar.vue",
        ),
        (
            custom_src / "SidebarLink.vue",
            education_src / "components" / "SidebarLink.vue",
        ),
        (
            custom_src / "StudentDashboard.vue",
            education_src / "pages" / "StudentDashboard.vue",
        ),
        (
            custom_src / "Attendance.vue",
            education_src / "pages" / "Attendance.vue",
        ),
        (
            custom_src / "router.js",
            education_src / "router.js",
        ),
    ]

    copied_files = []

    for source, destination in files_to_copy:

        if not source.exists():
            frappe.log_error(
                f"Missing override file:\n{source}",
                "Student Profile Override",
            )
            continue

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copy2(source, destination)

        copied_files.append(source.name)

        frappe.logger().info(
            f"Copied {source} -> {destination}"
        )

    frappe.logger().info(
        f"Education overrides applied successfully. Files: {copied_files}"
    )

    build_education_frontend(bench_path)


def build_education_frontend(bench_path):
    """
    Build Education frontend.
    """

    frontend_path = (
        bench_path
        / "apps"
        / "education"
        / "frontend"
    )

    package_json = frontend_path / "package.json"

    if not package_json.exists():
        frappe.throw(
            f"package.json not found:\n{package_json}"
        )

    try:

        frappe.logger().info(
            f"Building Education frontend from: {frontend_path}"
        )

        subprocess.run(
            ["npm", "install"],
            cwd=frontend_path,
            check=True,
        )

        subprocess.run(
            ["npm", "run", "build"],
            cwd=frontend_path,
            check=True,
        )

        frappe.logger().info(
            "Education frontend build completed successfully"
        )

    except subprocess.CalledProcessError as e:

        frappe.log_error(
            frappe.get_traceback(),
            "Education Frontend Build Failed",
        )

        raise e