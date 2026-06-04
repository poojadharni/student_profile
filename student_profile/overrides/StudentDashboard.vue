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

                    <div @click="activeTab = 'personal'" class="cursor-pointer text-xs font-semibold pb-1" :class="activeTab === 'personal'
                        ? 'text-emerald-600 border-b-2 border-emerald-600'
                        : 'text-gray-600'
                        ">
                        Personal
                    </div>

                    <div @click="activeTab = 'contact'" class="cursor-pointer text-xs font-semibold pb-1" :class="activeTab === 'contact'
                        ? 'text-emerald-600 border-b-2 border-emerald-600'
                        : 'text-gray-600'
                        ">
                        Contact
                    </div>

                    <div @click="activeTab = 'academic'" class="cursor-pointer text-xs font-semibold pb-1" :class="activeTab === 'academic'
                        ? 'text-emerald-600 border-b-2 border-emerald-600'
                        : 'text-gray-600'
                        ">
                        Academic
                    </div>

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
const activeTab = ref('personal')

const personalDetails = computed(() => [
    {
        label: 'Student ID',
        value: studentData.value.name || '-',
    },
    {
        label: 'Full Name',
        value: studentData.value.student_name || '-',
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
    }
])

const contactDetails = computed(() => [
    {
        label: 'Mobile Number',
        value: studentData.value.student_mobile_number || '-',
    },
    {
        label: 'Email Address',
        value: studentData.value.student_email_id || '-',
    },
    {
        label: 'Address Line 1',
        value: studentData.value.address_line_1 || '-',
    },
    {
        label: 'Address Line 2',
        value: studentData.value.address_line_2 || '-',
    },
    {
        label: 'City',
        value: studentData.value.city || '-',
    },
    {
        label: 'State',
        value: studentData.value.state || '-',
    },
    {
        label: 'Country',
        value: studentData.value.country || '-',
    },
    {
        label: 'Pincode',
        value: studentData.value.pincode || '-',
    }
])

const academicDetails = computed(() => [
    {
        label: 'Class',
        value:
            studentData.value.current_program?.program ||
            studentData.value.custom_class ||
            '-',
    },
    {
        label: 'Batch',
        value:
            studentData.value.current_program?.student_batch ||
            studentData.value.custom_batch ||
            '-',
    },
    {
        label: 'Joining Date',
        value: studentData.value.joining_date || '-',
    },
    {
        label: 'Student Group',
        value:
            studentData.value.student_groups?.[0]?.label || '-',
    }
])

const details = computed(() => {
    if (activeTab.value === 'contact') {
        return contactDetails.value
    }

    if (activeTab.value === 'academic') {
        return academicDetails.value
    }

    return personalDetails.value
})

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
const feeDetails = ref([])

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
            `/api/method/education.education.api.get_student_invoices?student=${encodeURIComponent(studentData.value.name)}`
        )

        const result = await response.json()

        console.log('Fee API:', result)

        const invoices = result.message?.invoices || []

        feeDetails.value = invoices.map(invoice => ({
            month: invoice.payment_date
                ? new Date(invoice.payment_date).toLocaleString('default', {
                    month: 'long'
                })
                : '-',

            total: Number(
                String(invoice.amount)
                    .replace('₹', '')
                    .replace(/,/g, '')
            ),

            paid:
                invoice.status === 'Paid'
                    ? Number(
                        String(invoice.amount)
                            .replace('₹', '')
                            .replace(/,/g, '')
                    )
                    : 0,

            due:
                invoice.status !== 'Paid'
                    ? Number(
                        String(invoice.amount)
                            .replace('₹', '')
                            .replace(/,/g, '')
                    )
                    : 0,
        }))

        totalFee.value = feeDetails.value
            .reduce((sum, row) => sum + row.total, 0)
            .toLocaleString('en-IN')

        paidFee.value = feeDetails.value
            .reduce((sum, row) => sum + row.paid, 0)
            .toLocaleString('en-IN')

        dueFee.value = feeDetails.value
            .reduce((sum, row) => sum + row.due, 0)
            .toLocaleString('en-IN')

    } catch (error) {
        console.error('Fee API Error:', error)
    }
}

const fetchAttendanceSummary = async () => {
    try {

        if (!studentData.value.name) return

        const student = studentData.value.name

        const studentGroup =
            studentData.value.student_groups?.[0]?.label || ''

        console.log('Student:', student)
        console.log('Student Group:', studentGroup)

        if (!studentGroup) {
            console.warn('Student Group not found')
            return
        }

        const response = await fetch(
            `/api/method/education.education.api.get_student_attendance?student=${encodeURIComponent(
                student
            )}&student_group=${encodeURIComponent(
                studentGroup
            )}`
        )

        const result = await response.json()

        console.log('Attendance API:', result)

        const rows = result.message || []

        const present = rows.filter(
            row => row.status === 'Present'
        ).length

        const absent = rows.filter(
            row => row.status === 'Absent'
        ).length

        const leave = rows.filter(
            row => row.status === 'Leave'
        ).length

        attendanceSeries.value = [
            {
                name: 'Days Present',
                data: [present]
            },
            {
                name: 'Days Absent',
                data: [absent]
            },
            {
                name: 'Leaves',
                data: [leave]
            }
        ]

        attendanceChartOptions.value = {
            ...attendanceChartOptions.value,
            xaxis: {
                categories: ['Attendance'],
                max: present + absent + leave
            }
        }

    } catch (error) {
        console.error('Attendance Error:', error)
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
const attendanceSeries = ref([
    {
        name: 'Days Present',
        data: [0],
    },
    {
        name: 'Days Absent',
        data: [0],
    },
    {
        name: 'Leaves',
        data: [0],
    },
])

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
    await fetchAttendanceSummary()
})
</script>