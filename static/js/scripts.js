document.addEventListener('DOMContentLoaded', function () {
    const borrowList = document.getElementById('borrowList');
    const addMemberForm = document.getElementById('addMemberForm');

    // Dữ liệu mẫu
    let members = [
        { id: 1, name: 'Lê Văn A', dob: '2000-01-01', address: 'Hà Nội', book: 'Python Cơ Bản', date: '2024-10-26', status: 'Đang mượn' },
        { id: 2, name: 'Trần Thị B', dob: '1995-05-10', address: 'TP. HCM', book: 'Lập Trình C++', date: '2024-10-24', status: 'Đã trả' },
    ];

    // Hàm hiển thị dữ liệu
    function renderTable() {
        borrowList.innerHTML = '';
        members.forEach((member, index) => {
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${member.name}</td>
                <td>${member.dob}</td>
                <td>${member.address}</td>
                <td>${member.book}</td>
                <td>${member.date}</td>
                <td>${member.status}</td>
                <td>
                    <button class="edit-btn" onclick="editMember(${member.id})">Sửa</button>
                    <button class="delete-btn" onclick="deleteMember(${member.id})">Xóa</button>
                    <button class="status-btn" onclick="toggleStatus(${member.id})">Đổi Trạng Thái</button>
                </td>
            `;
            borrowList.appendChild(row);
        });
    }

    // Hàm thêm thành viên mới
    addMemberForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const newMember = {
            id: members.length + 1,
            name: document.getElementById('memberName').value,
            dob: document.getElementById('memberDob').value,
            address: document.getElementById('memberAddress').value,
            book: document.getElementById('bookTitle').value,
            date: document.getElementById('borrowDate').value,
            status: 'Đang mượn'
        };
        members.push(newMember);
        renderTable();
        addMemberForm.reset();
    });

    // Hàm sửa thành viên
    window.editMember = function (id) {
        const member = members.find(m => m.id === id);
        if (member) {
            document.getElementById('memberName').value = member.name;
            document.getElementById('memberDob').value = member.dob;
            document.getElementById('memberAddress').value = member.address;
            document.getElementById('bookTitle').value = member.book;
            document.getElementById('borrowDate').value = member.date;
            deleteMember(id);
        }
    }

    // Hàm xóa thành viên
    window.deleteMember = function (id) {
        members = members.filter(m => m.id !== id);
        renderTable();
    }

    // Hàm thay đổi trạng thái
    window.toggleStatus = function (id) {
        const member = members.find(m => m.id === id);
        if (member) {
            member.status = (member.status === 'Đang mượn') ? 'Đã trả' : 'Đang mượn';
            renderTable();
        }
    }

    // Hiển thị dữ liệu lần đầu
    renderTable();
});
