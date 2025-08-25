document.addEventListener('DOMContentLoaded', function () {
    // Size selection
    const sizeButtons = document.querySelectorAll('.size-btn');
    let selectedSize = '';

    sizeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            sizeButtons.forEach(b => b.classList.remove('border-pink-400', 'bg-pink-50', 'text-pink-700'));
            btn.classList.add('border-pink-400', 'bg-pink-50', 'text-pink-700');
            selectedSize = btn.dataset.size;
        });
    });

    if (sizeButtons.length > 0) {
        sizeButtons[0].click();
    }

    // Add to wishlist with modal
    const addToCartBtn = document.getElementById('addToCartBtn');
    const successModal = document.getElementById('successModal');
    const continueShopping = document.getElementById('continueShopping');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    if (addToCartBtn) {
        addToCartBtn.addEventListener('click', async function() {
            if (!selectedSize && sizeButtons.length > 0) {
                selectedSize = sizeButtons[0].dataset.size;
                sizeButtons[0].click();
            }

            try {
                const csrftoken = getCookie('csrftoken');

                const response = await fetch(addToCartBtn.dataset.url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                    body: JSON.stringify({ size: selectedSize })
                });

                if (response.ok) {
                    successModal.classList.remove('hidden');
                } else {
                    alert('Грешка при додавање во кошничка.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Грешка при додавање во кошничка.');
            }
        });
    }

    if (continueShopping) {
        continueShopping.addEventListener('click', function() {
            successModal.classList.add('hidden');
        });
    }

    successModal.addEventListener('click', function(e) {
        if (e.target === successModal) {
            successModal.classList.add('hidden');
        }
    });
});
