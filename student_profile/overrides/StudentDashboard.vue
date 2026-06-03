<template>
    <div class="min-h-screen bg-[#f5f5f7] p-2 md:p-4">
        <!-- TOP SECTION -->
        <div class="grid grid-cols-1 xl:grid-cols-12 gap-3 mb-3">

            <!-- LEFT PROFILE -->
            <div class="xl:col-span-2 bg-white border rounded-xl p-3 shadow-sm">
                <label class="text-xs font-semibold text-gray-700 block mb-2">
                    {{ studentData?.student_name || 'Student Profile' }} </label>
                <!-- STUDENT IMAGE -->
                <img class="w-full h-52 object-cover rounded-lg" :src="studentData.image ||
                    'https://images.unsplash.com/photo-1619895862022-09114b41f16f?q=80&w=1200&auto=format&fit=crop'
                    " />
            </div>

            <!-- STUDENT DETAILS -->
            <div class="xl:col-span-4 bg-white border rounded-xl p-3 shadow-sm">

                <!-- TABS -->
                <div class="flex flex-wrap gap-5 border-b pb-2 mb-3">

                    <button class="text-xs font-semibold text-emerald-600 border-b-2 border-emerald-600 pb-1">
                        Personal
                    </button>

                    <button class="text-xs font-semibold text-gray-600">
                        Contact
                    </button>

                    <button class="text-xs font-semibold text-gray-600">
                        Academic
                    </button>

                </div>

                <!-- DETAILS TABLE -->
                <div class="border border-gray-200 rounded-lg overflow-hidden">

                    <div v-for="item in details" :key="item.label" class="grid grid-cols-2 border-b last:border-b-0">

                        <div class="border-r bg-gray-50 px-3 py-2 text-[11px] md:text-xs font-semibold text-gray-700">
                            {{ item.label }}
                        </div>

                        <div class="px-3 py-2 text-[11px] md:text-xs text-gray-600 break-words">
                            {{ item.value }}
                        </div>

                    </div>

                </div>

            </div>

            <!-- RIGHT SECTION -->
            <div class="xl:col-span-6 flex flex-col gap-3">

                <!-- STATS -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

                    <div class="rounded-xl p-4 text-center bg-gradient-to-r from-pink-500 to-rose-500 shadow-sm">

                        <p class="text-xs text-white/80 mb-1">
                            Student Suspension Rate
                        </p>

                        <h2 class="text-2xl font-bold text-white">
                            2.44%
                        </h2>

                    </div>

                    <div class="rounded-xl p-4 text-center bg-gradient-to-r from-cyan-500 to-blue-500 shadow-sm">

                        <p class="text-xs text-white/80 mb-1">
                            Class Participation Rate
                        </p>

                        <h2 class="text-2xl font-bold text-white">
                            87.48%
                        </h2>

                    </div>

                </div>

                <!-- ATTENDANCE -->
                <div class="bg-white border rounded-xl p-3 shadow-sm">

                    <div class="text-sm font-semibold mb-3 text-gray-700">
                        Attendance Summary
                    </div>

                    <!-- LEGEND -->
                    <div class="flex flex-wrap justify-center gap-4 md:gap-5 text-[10px] md:text-[11px] mb-3">

                        <div class="flex items-center gap-1">
                            <div class="w-2 h-2 rounded-full bg-red-400"></div>
                            Days Absent
                        </div>

                        <div class="flex items-center gap-1">
                            <div class="w-2 h-2 rounded-full bg-emerald-400"></div>
                            Days Present
                        </div>

                        <div class="flex items-center gap-1">
                            <div class="w-2 h-2 rounded-full bg-yellow-400"></div>
                            Leaves
                        </div>

                    </div>

                    <apexchart type="bar" height="180" :options="attendanceChartOptions" :series="attendanceSeries" />

                </div>

            </div>

        </div>

        <!-- BOTTOM SECTION -->
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-3 items-start mb-3">

            <!-- FEE SUMMARY -->
            <div class="bg-white border rounded-xl p-3 shadow-sm">

                <div class="flex items-center justify-between mb-3">

                    <h2 class="text-sm font-semibold text-gray-700">
                        Student Fee Summary
                    </h2>

                    <span class="text-[11px] text-gray-400">
                        Academic Year 2025
                    </span>

                </div>

                <!-- TABLE -->
                <div class="overflow-x-auto border rounded-lg">

                    <div class="min-w-[500px]">

                        <!-- HEADER -->
                        <div class="grid grid-cols-4 bg-gray-100 border-b text-[11px] font-semibold text-gray-700">

                            <div class="px-2 py-2 border-r">
                                Month
                            </div>

                            <div class="px-2 py-2 border-r">
                                Total Fee
                            </div>

                            <div class="px-2 py-2 border-r">
                                Paid Fee
                            </div>

                            <div class="px-2 py-2">
                                Due Fee
                            </div>

                        </div>

                        <!-- ROWS -->
                        <div v-for="fee in feeDetails" :key="fee.month"
                            class="grid grid-cols-4 text-[11px] border-b last:border-b-0">

                            <div class="px-2 py-2 border-r">
                                {{ fee.month }}
                            </div>

                            <div class="px-2 py-2 border-r text-blue-600 font-medium">
                                ₹ {{ fee.total }}
                            </div>

                            <div class="px-2 py-2 border-r text-emerald-600 font-medium">
                                ₹ {{ fee.paid }}
                            </div>

                            <div class="px-2 py-2 text-red-500 font-medium">
                                ₹ {{ fee.due }}
                            </div>

                        </div>

                    </div>

                </div>

                <!-- SUMMARY -->
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 mt-3">

                    <div class="bg-blue-50 rounded-xl p-3 text-center">

                        <p class="text-[10px] text-gray-500">
                            Total Fee
                        </p>

                        <h3 class="text-sm font-bold text-blue-600">
                            ₹ {{ totalFee }}
                        </h3>

                    </div>

                    <div class="bg-emerald-50 rounded-xl p-3 text-center">

                        <p class="text-[10px] text-gray-500">
                            Paid Fee
                        </p>

                        <h3 class="text-sm font-bold text-emerald-600">
                            ₹ {{ paidFee }}
                        </h3>

                    </div>

                    <div class="bg-red-50 rounded-xl p-3 text-center">

                        <p class="text-[10px] text-gray-500">
                            Due Fee
                        </p>

                        <h3 class="text-sm font-bold text-red-500">
                            ₹ {{ dueFee }}
                        </h3>

                    </div>

                </div>

            </div>

            <!-- SUBJECT GRADE -->
            <div class="bg-white border rounded-xl p-3 shadow-sm">

                <div class="text-sm font-semibold mb-3 text-gray-700">
                    Grade by Subject
                </div>

                <apexchart type="bar" height="260" :options="gradeChartOptions" :series="gradeSeries" />
            </div>

        </div>

        <!-- NOTIFICATIONS -->
        <div class="mt-3">
            <div class="bg-white border rounded-xl p-4 shadow-sm">

                <!-- HEADER -->
                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 mb-4">

                    <div>
                        <h2 class="text-sm font-semibold text-gray-800">
                            Recent Notifications
                        </h2>
                        <p class="text-[11px] text-gray-400">
                            Student updates & activities
                        </p>
                    </div>

                    <button class="text-[11px] bg-blue-50 text-blue-600 px-3 py-1 rounded-full w-fit">
                        View All
                    </button>

                </div>

                <!-- GRID -->
                <div class="grid grid-cols-1 xl:grid-cols-4 gap-3">

                    <!-- 📝 EXAM CARD -->
                    <div v-if="notifications.exam.length"
                        class="bg-blue-50 border border-blue-100 rounded-xl p-3 shadow-sm">

                        <h2 class="text-sm font-semibold mb-3 text-blue-700">
                            Exam Schedule
                        </h2>

                        <div v-for="n in notifications.exam" :key="n.id" @click="openNotification(n)"
                            class="group cursor-pointer rounded-lg border bg-white hover:shadow-md hover:border-blue-300 transition-all p-3 mb-2">

                            <div class="flex items-start justify-between mb-2">

                                <div class="w-8 h-8 rounded-lg flex items-center justify-center text-white bg-blue-500">
                                    📝
                                </div>

                                <span class="text-[10px] text-gray-400">
                                    {{ n.time }}
                                </span>

                            </div>

                            <h3 class="text-xs font-semibold text-gray-800 group-hover:text-blue-600">
                                {{ n.title }}
                            </h3>

                            <p class="text-[11px] text-gray-500 line-clamp-2">
                                {{ n.message }}
                            </p>

                        </div>
                    </div>

                    <!-- 💳 FEE CARD -->
                    <div v-if="notifications.fee.length"
                        class="bg-green-50 border border-green-100 rounded-xl p-3 shadow-sm">

                        <h2 class="text-sm font-semibold mb-3 text-green-700">
                            Fee Alerts
                        </h2>

                        <div v-for="n in notifications.fee" :key="n.id" @click="openNotification(n)"
                            class="group cursor-pointer rounded-lg border bg-white hover:shadow-md hover:border-green-300 transition-all p-3 mb-2">

                            <div class="flex items-start justify-between mb-2">

                                <div
                                    class="w-8 h-8 rounded-lg flex items-center justify-center text-white bg-green-500">
                                    💳
                                </div>

                                <span class="text-[10px] text-gray-400">
                                    {{ n.time }}
                                </span>

                            </div>

                            <h3 class="text-xs font-semibold text-gray-800 group-hover:text-green-600">
                                {{ n.title }}
                            </h3>

                            <p class="text-[11px] text-gray-500 line-clamp-2">
                                {{ n.message }}
                            </p>

                        </div>
                    </div>

                    <!-- 📊 ATTENDANCE CARD -->
                    <div v-if="notifications.attendance.length"
                        class="bg-yellow-50 border border-yellow-100 rounded-xl p-3 shadow-sm">

                        <h2 class="text-sm font-semibold mb-3 text-yellow-700">
                            Attendance
                        </h2>

                        <div v-for="n in notifications.attendance" :key="n.id" @click="openNotification(n)"
                            class="group cursor-pointer rounded-lg border bg-white hover:shadow-md hover:border-yellow-300 transition-all p-3 mb-2">

                            <div class="flex items-start justify-between mb-2">

                                <div
                                    class="w-8 h-8 rounded-lg flex items-center justify-center text-white bg-yellow-500">
                                    📊
                                </div>

                                <span class="text-[10px] text-gray-400">
                                    {{ n.time }}
                                </span>

                            </div>

                            <h3 class="text-xs font-semibold text-gray-800 group-hover:text-yellow-600">
                                {{ n.title }}
                            </h3>

                            <p class="text-[11px] text-gray-500 line-clamp-2">
                                {{ n.message }}
                            </p>

                        </div>
                    </div>

                    <!-- 🎉 EVENTS CARD -->
                    <div v-if="notifications.events.length"
                        class="bg-purple-50 border border-purple-100 rounded-xl p-3 shadow-sm">

                        <h2 class="text-sm font-semibold mb-3 text-purple-700">
                            Events
                        </h2>

                        <div v-for="n in notifications.events" :key="n.id" @click="openNotification(n)"
                            class="group cursor-pointer rounded-lg border bg-white hover:shadow-md hover:border-purple-300 transition-all p-3 mb-2">

                            <div class="flex items-start justify-between mb-2">

                                <div
                                    class="w-8 h-8 rounded-lg flex items-center justify-center text-white bg-purple-500">
                                    🎉
                                </div>

                                <span class="text-[10px] text-gray-400">
                                    {{ n.time }}
                                </span>

                            </div>

                            <h3 class="text-xs font-semibold text-gray-800 group-hover:text-purple-600">
                                {{ n.title }}
                            </h3>

                            <p class="text-[11px] text-gray-500 line-clamp-2">
                                {{ n.message }}
                            </p>

                        </div>
                    </div>

                </div>
            </div>
        </div>

        <!-- MODAL -->
        <div v-if="showModal"
            class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 px-3">

            <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-5">

                <!-- TOP -->
                <div class="flex items-start justify-between mb-4">

                    <div class="flex items-center gap-3">

                        <div class="w-12 h-12 rounded-xl flex items-center justify-center text-2xl text-white"
                            :class="selectedNotification.bg">

                            {{ selectedNotification.icon }}

                        </div>

                        <div>

                            <h2 class="text-base md:text-lg font-semibold text-gray-800">
                                {{ selectedNotification.title }}
                            </h2>

                            <p class="text-xs text-gray-400">
                                {{ selectedNotification.time }}
                            </p>

                        </div>

                    </div>

                    <button @click="showModal = false" class="text-gray-400 hover:text-red-500 text-xl">

                        ×
                    </button>

                </div>

                <!-- BODY -->
                <div class="bg-gray-50 border rounded-xl p-4 text-sm text-gray-600 leading-7">
                    {{ selectedNotification.message }}
                </div>

                <!-- FOOTER -->
                <div class="mt-5 text-right">

                    <button @click="showModal = false"
                        class="bg-blue-500 hover:bg-blue-600 transition text-white text-sm px-5 py-2 rounded-lg">

                        Close
                    </button>

                </div>

            </div>

        </div>

    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

/* ----------------------------------
   STUDENT DATA
---------------------------------- */
const studentData = ref({})

const details = computed(() => [
    {
        label: 'Student ID',
        value: studentData.value.name || '-',
    },
    {
        label: 'Full Name',
        value: studentData.value.student_name || '-',
    },
    {
        label: 'Grade',
        value:
            studentData.value.current_program?.program ||
            studentData.value.custom_class ||
            '-',
    },
    {
        label: 'Age',
        value: studentData.value.age || '-',
    },
    {
        label: 'Gender',
        value: studentData.value.gender || '-',
    },
    {
        label: 'Nationality',
        value: studentData.value.nationality || 'Indian',
    },
    {
        label: 'Email Address',
        value:
            studentData.value.student_email_id ||
            studentData.value.email ||
            '-',
    },
])

/* ----------------------------------
   FETCH STUDENT INFO
---------------------------------- */
const fetchStudentInfo = async () => {
    try {
        const response = await fetch(
            '/api/method/education.education.api.get_student_info'
        )

        const result = await response.json()

        console.log('Student Data:', result)

        if (result.message) {
            studentData.value = result.message
        }
    } catch (error) {
        console.error('Student Info Error:', error)
    }
}
const fetchStudentGrades = async () => {
    try {

        if (!studentData.value.name) return

        const response = await fetch(
            '/api/method/frappe.client.get_list?' +
            new URLSearchParams({
                doctype: 'Assessment Result',
                fields: JSON.stringify([
                    'course',
                    'grade',
                    'total_score',
                    'maximum_score'
                ]),
                filters: JSON.stringify({
                    student: studentData.value.name
                }),
                limit_page_length: 100
            })
        )

        const result = await response.json()

        console.log('Grade Data:', result)

        const grades = result.message || []

        gradeChartOptions.value = {
            ...gradeChartOptions.value,
            xaxis: {
                categories: grades.map(row => row.course)
            }
        }

        gradeSeries.value = [
            {
                name: 'Score',
                data: grades.map(row => {
                    const score = Number(row.total_score || 0)
                    const max = Number(row.maximum_score || 0)

                    return max > 0
                        ? ((score / max) * 100).toFixed(2)
                        : 0
                })
            }
        ]

    } catch (error) {
        console.error('Grade API Error:', error)
    }
}
const stripHtml = (html) => {
    const div = document.createElement('div')
    div.innerHTML = html || ''
    return div.textContent || div.innerText || ''
}

const fetchNotifications = async () => {
    try {
        const response = await fetch(
            '/api/method/frappe.desk.doctype.notification_log.notification_log.get_notification_logs'
        )

        const result = await response.json()

        const logs = result.message?.notification_logs || []

        const grouped = {
            exam: [],
            fee: [],
            attendance: [],
            events: [],
        }

        logs.forEach((item) => {
            const clean = {
                id: item.name,
                title: item.subject || 'Notification',
                time: new Date(item.creation).toLocaleString(),
                message: stripHtml(item.email_content),
                fullContent: item.email_content,
                documentType: item.document_type,
            }

            // 📝 Exam
            if (item.document_type === 'Assessment Plan') {
                grouped.exam.push(clean)
            }

            // 💳 Fee (if you have fee notifications)
            else if (item.document_type === 'Fees' || item.subject?.includes('Fee')) {
                grouped.fee.push(clean)
            }

            // 📊 Attendance
            else if (item.document_type === 'Attendance') {
                grouped.attendance.push(clean)
            }

            // 🎉 EVENTS (IMPORTANT PART)
            else if (
                item.document_type === 'Event' ||
                item.document_type === 'Calendar Event' ||
                item.subject?.toLowerCase().includes('event')
            ) {
                grouped.events.push(clean)
            }
        })

        notifications.value = grouped
    } catch (error) {
        console.error('Notification API Error:', error)
    }
}
/* ----------------------------------
   FEE DETAILS
---------------------------------- */
const feeDetails = ref([
    { month: 'January', total: '0', paid: '0', due: '0' },
    { month: 'February', total: '0', paid: '0', due: '0' },
    { month: 'March', total: '0', paid: '0', due: '0' },
    { month: 'April', total: '0', paid: '0', due: '0' },
    { month: 'May', total: '0', paid: '0', due: '0' },
    { month: 'June', total: '0', paid: '0', due: '0' },
])

const totalFee = ref(0)
const paidFee = ref(0)
const dueFee = ref(0)

/* ----------------------------------
   FETCH FEES
---------------------------------- */
const fetchFeeSummary = async () => {
    try {
        if (!studentData.value.name) return

        const response = await fetch(
            '/api/method/education.education.api.get_student_invoices',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    student: studentData.value.name,
                }),
            }
        )

        const result = await response.json()

        const invoices = result.message || []

        const monthMap = {}

        let total = 0
        let paid = 0
        let due = 0

        invoices.forEach((inv) => {
            const grandTotal = Number(inv.grand_total || 0)
            const outstanding = Number(inv.outstanding_amount || 0)
            const status = inv.status

            const month = new Date(inv.creation).toLocaleString('default', {
                month: 'long',
            })

            // 👉 create month only when data exists
            if (!monthMap[month]) {
                monthMap[month] = {
                    total: 0,
                    paid: 0,
                    due: 0,
                }
            }

            monthMap[month].total += grandTotal

            if (status === 'Paid') {
                monthMap[month].paid += grandTotal
            }

            monthMap[month].due += outstanding

            total += grandTotal
            if (status === 'Paid') paid += grandTotal
            due += outstanding
        })

        // 👉 convert only existing months (no empty months)
        feeDetails.value = Object.keys(monthMap).map((month) => ({
            month,
            total: monthMap[month].total.toLocaleString('en-IN'),
            paid: monthMap[month].paid.toLocaleString('en-IN'),
            due: monthMap[month].due.toLocaleString('en-IN'),
        }))

        totalFee.value = total.toLocaleString('en-IN')
        paidFee.value = paid.toLocaleString('en-IN')
        dueFee.value = due.toLocaleString('en-IN')
    } catch (error) {
        console.error('Student Fee API Error:', error)
    }
}

/* ----------------------------------
   NOTIFICATIONS
---------------------------------- */
const notifications = ref({
    exam: [],
    fee: [],
    attendance: [],
    events: []
})
const showModal = ref(false)

const selectedNotification = ref({})

const openNotification = (notification) => {
    selectedNotification.value = notification
    showModal.value = true
}

/* ----------------------------------
   CHARTS
---------------------------------- */
const attendanceSeries = [
    {
        name: 'Days Present',
        data: [85],
    },
    {
        name: 'Days Absent',
        data: [8],
    },
    {
        name: 'Leaves',
        data: [7],
    },
]

const attendanceChartOptions = {
    chart: {
        toolbar: {
            show: false,
        },
    },
    plotOptions: {
        bar: {
            horizontal: true,
            borderRadius: 4,
            barHeight: '55%',
        },
    },
    colors: ['#43d3ac', '#ef6a6a', '#facc15'],
    dataLabels: {
        enabled: false,
    },
    legend: {
        show: false,
    },
    xaxis: {
        categories: [''],
        max: 100,
    },
}

const gradeSeries = ref([
    {
        name: 'Score',
        data: [],
    },
])

const gradeChartOptions = ref({
    chart: {
        toolbar: {
            show: false,
        },
    },

    colors: ['#3fc8be'],

    plotOptions: {
        bar: {
            borderRadius: 4,
            columnWidth: '55%',
        },
    },

    dataLabels: {
        enabled: true,
        formatter: (val) => `${val}%`,
    },

    yaxis: {
        max: 100,
    },

    xaxis: {
        categories: [],
    },

    grid: {
        borderColor: '#eee',
    },
})

/* ----------------------------------
   PAGE LOAD
---------------------------------- */
onMounted(async () => {
    await fetchStudentInfo()
    await fetchStudentGrades()
    await fetchNotifications()
    await fetchFeeSummary()
})
</script>