<template>
  <div>
    <!-- The Modal -->
    <div id="base-modal" class="modal display-block">
      <!-- Modal Header -->
      <div class="modal-content">
        <div class="modal-header">
          {{ title }}
        </div>
        <!-- Modal Body -->
        <div class="modal-body">
          <slot></slot>
        </div>
        <!-- Modal Footer -->
        <div class="modal-footer">
          <slot name="footer"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      required: true,
      type: String
    }
  }
};
</script>

<style scoped>

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 9999; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
  position: relative;
  background-color: #fefefe;
  margin: auto;
  padding: 0;
  border: 1px solid #888;
  max-width: 960px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  -webkit-animation-name: animatetop;
  -webkit-animation-duration: 0.4s;
  animation-name: animatetop;
  animation-duration: 0.4s
}

/* Add Animation */
@-webkit-keyframes animatetop {
  from {
    top: -300px;
    opacity: 0
  }
  to {
    top: 0;
    opacity: 1
  }
}

@keyframes animatetop {
  from {
    top: -300px;
    opacity: 0
  }
  to {
    top: 0;
    opacity: 1
  }
}

.modal-header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 18px;
  color: #444;
  font-size: 24px;
  font-weight: bold;
  border-bottom: solid 1px #7c7c7c;

}

.modal-body {
  padding: 60px;
}

.modal-footer {
  padding: 2px 16px;
  color: #444;
  border: unset;
}

.display-block {
  display: block;
}

@media (max-width: 768px) {
  .modal-body {
    padding: 10px;
  }

  .modal-header{
    padding: 10px;
  }

  .modal-content {
    max-width: 350px;
  }

  .modal{
    padding-top: 40px;
  }
}
</style>
