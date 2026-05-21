import os
import re

file_path = '/Users/pusthe_nihal/Downloads/services.html'

with open(file_path, 'r') as f:
    content = f.read()

# Replace the buttons
content = content.replace(
    '<button class="w-full py-3.5 rounded-xl font-bold text-sm bg-accent text-white hover:bg-accent-dark transition-all duration-200 shadow-md shadow-accent/20">Get This Package</button>',
    '<button id="btn-standard" class="w-full py-3.5 rounded-xl font-bold text-sm bg-accent text-white hover:bg-accent-dark transition-all duration-200 shadow-md shadow-accent/20">Get This Package</button>',
    1
)

content = content.replace(
    '<button class="w-full py-3.5 rounded-xl font-bold text-sm bg-accent text-white hover:bg-accent-dark transition-all duration-200 shadow-md shadow-accent/20">Get This Package</button>',
    '<button id="btn-deluxe" class="w-full py-3.5 rounded-xl font-bold text-sm bg-accent text-white hover:bg-accent-dark transition-all duration-200 shadow-md shadow-accent/20">Get This Package</button>',
    1
)

content = content.replace(
    '<button class="w-full py-3.5 rounded-xl font-bold text-sm bg-accent text-white hover:bg-accent-dark transition-all duration-200 shadow-md shadow-accent/20">Get This Package</button>',
    '<button id="btn-premium" class="w-full py-3.5 rounded-xl font-bold text-sm bg-accent text-white hover:bg-accent-dark transition-all duration-200 shadow-md shadow-accent/20">Get This Package</button>',
    1
)

content = content.replace(
    '<button class="w-full py-3.5 rounded-xl font-bold text-sm bg-amber-300 text-accent hover:bg-amber-400 transition-all duration-200 shadow-md shadow-black/10">Get This Package</button>',
    '<button id="btn-ultra" class="w-full py-3.5 rounded-xl font-bold text-sm bg-amber-300 text-accent hover:bg-amber-400 transition-all duration-200 shadow-md shadow-black/10">Get This Package</button>',
    1
)

new_modals = """
  <!-- Standard Modal -->
  <div id="modal-standard" class="fixed inset-0 z-[100] flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-300">
    <div class="absolute inset-0 bg-gray-900/40 backdrop-blur-sm modal-bg-close"></div>
    <div class="relative bg-white w-full max-w-lg rounded-2xl shadow-2xl p-8 transform scale-95 transition-transform duration-300 overflow-y-auto max-h-[90vh] modal-content-box">
      <button class="absolute top-4 right-4 text-gray-400 hover:text-gray-900 transition-colors modal-close-btn">
        <iconify-icon icon="lucide:x" class="text-xl"></iconify-icon>
      </button>
      <h3 class="font-display text-2xl font-bold mb-1">Standard Package Form</h3>
      <p class="text-[11px] font-bold uppercase tracking-wider text-accent mb-2">Simple & Fast Lead Capture</p>
      <p class="text-sm text-gray-500 mb-6">Best for smaller builders who want quick communication.</p>
      
      <form class="space-y-4">
        <div class="grid grid-cols-2 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Full Name</label><input type="text" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Company Name</label><input type="text" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Phone Number</label><input type="tel" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Email Address</label><input type="email" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Project Location</label><input type="text" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Number of Rooms</label><input type="number" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Property Type</label>
            <select class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required><option value="" disabled selected>Select</option><option>Villa</option><option>Small Apartment</option><option>Plot Layout</option><option>Interior Only</option></select>
          </div>
          <div>
            <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Need Exterior Add-on?</label>
            <select class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required><option value="" disabled selected>Select</option><option>Yes</option><option>No</option></select>
          </div>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Upload Floor Plan</label>
          <input type="file" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-bold file:bg-surface-warm file:text-accent hover:file:bg-surface-warm/80">
        </div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Additional Notes</label>
          <textarea rows="2" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all resize-none"></textarea>
        </div>
        <button type="submit" class="w-full py-3 mt-2 bg-accent text-white font-bold rounded-xl hover:bg-accent-dark transition-all duration-200 shadow-lg shadow-accent/25 text-sm">Get My Presentation Started</button>
        <p class="text-[11px] font-bold text-center text-gray-400 mt-3">Ideal for fast-moving projects with essential presentation needs.</p>
      </form>
    </div>
  </div>

  <!-- Deluxe Modal -->
  <div id="modal-deluxe" class="fixed inset-0 z-[100] flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-300">
    <div class="absolute inset-0 bg-gray-900/50 backdrop-blur-md modal-bg-close"></div>
    <div class="relative bg-white w-full max-w-lg rounded-2xl shadow-2xl p-8 transform scale-95 transition-transform duration-300 overflow-y-auto max-h-[90vh] modal-content-box border-t-4 border-accent">
      <button class="absolute top-4 right-4 text-gray-400 hover:text-gray-900 transition-colors modal-close-btn">
        <iconify-icon icon="lucide:x" class="text-xl"></iconify-icon>
      </button>
      <h3 class="font-display text-2xl font-bold mb-1">Deluxe Package Form</h3>
      <p class="text-[11px] font-bold uppercase tracking-wider text-accent mb-2">Interactive Experience Focus</p>
      <p class="text-sm text-gray-500 mb-6">This form should feel more premium and feature-oriented.</p>
      
      <form class="space-y-4">
        <div class="grid grid-cols-2 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Full Name</label><input type="text" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Company / Developer Name</label><input type="text" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Contact Number</label><input type="tel" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Email Address</label><input type="email" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        </div>
        <div class="grid grid-cols-3 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Project Type</label><input type="text" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Number of Floors</label><input type="number" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Total Units / Villas</label><input type="number" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Required Features</label>
          <div class="grid grid-cols-2 gap-2 text-sm text-gray-600">
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Exterior 360°</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Room Navigation</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Custom Flooring</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Wall Customization</label>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Preferred UI Style</label>
            <select class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required><option value="" disabled selected>Select style</option><option>Minimal</option><option>Luxury</option><option>Dark</option><option>Modern</option></select>
          </div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Expected Delivery Timeline</label><input type="text" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Upload Plans / CAD Files</label>
          <input type="file" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-bold file:bg-surface-warm file:text-accent hover:file:bg-surface-warm/80">
        </div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Additional Requirements</label>
          <textarea rows="2" class="w-full px-3 py-2 bg-surface-warm/50 border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all resize-none"></textarea>
        </div>
        <button type="submit" class="w-full py-3 mt-2 bg-accent text-white font-bold rounded-xl hover:bg-accent-dark transition-all duration-200 shadow-lg shadow-accent/25 text-sm">Build My Interactive Experience</button>
        <p class="text-[11px] font-bold text-center text-accent/70 mt-3 uppercase tracking-widest">Step 1 of 2 — Project Details</p>
      </form>
    </div>
  </div>

  <!-- Premium Modal -->
  <div id="modal-premium" class="fixed inset-0 z-[100] flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-300">
    <div class="absolute inset-0 bg-gray-900/60 backdrop-blur-md modal-bg-close"></div>
    <div class="relative bg-gray-50 w-full max-w-xl rounded-2xl shadow-2xl p-8 transform scale-95 transition-transform duration-300 overflow-y-auto max-h-[90vh] modal-content-box border border-black/10">
      <button class="absolute top-4 right-4 text-gray-400 hover:text-gray-900 transition-colors modal-close-btn">
        <iconify-icon icon="lucide:x" class="text-xl"></iconify-icon>
      </button>
      <div class="flex items-center gap-2 mb-1">
        <iconify-icon icon="lucide:crown" class="text-accent text-xl"></iconify-icon>
        <h3 class="font-display text-2xl font-bold">Premium Package Form</h3>
      </div>
      <p class="text-[11px] font-bold uppercase tracking-wider text-accent mb-2">Luxury + Pre-Construction Sales Focus</p>
      <p class="text-sm text-gray-500 mb-6">This should feel high-end and consultation-based.</p>
      
      <form class="space-y-4">
        <div class="grid grid-cols-2 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Full Name</label><input type="text" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Company Name</label><input type="text" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Designation</label><input type="text" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all"></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Phone Number</label><input type="tel" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div class="col-span-2"><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Email Address</label><input type="email" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Project Name</label><input type="text" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Number of BHK Variants</label><input type="text" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Project Scale</label>
            <select class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required><option value="" disabled selected>Select scale</option><option>Villas</option><option>Apartments</option><option>Township</option><option>Mixed Use</option></select>
          </div>
          <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Preferred Branding Style</label>
            <select class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required><option value="" disabled selected>Select style</option><option>Luxury</option><option>Corporate</option><option>Modern</option><option>Minimal</option></select>
          </div>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-2">Project Features Needed</label>
          <div class="grid grid-cols-2 gap-2 text-sm text-gray-600">
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Need Aerial View?</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Need Day/Night Mode?</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Need Custom Figma UI?</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Need Video Footage?</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded text-accent focus:ring-accent"> Need AI Chatbot?</label>
          </div>
        </div>
        <div><label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Expected Launch Date</label><input type="date" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all" required></div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Upload Branding / Floor Plans / References</label>
          <input type="file" multiple class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-bold file:bg-surface-warm file:text-accent hover:file:bg-surface-warm/80">
        </div>
        <div>
          <label class="block text-[11px] font-bold text-gray-500 uppercase mb-1.5">Describe Your Vision</label>
          <textarea rows="2" class="w-full px-3 py-2 bg-white border border-black/5 rounded-lg text-sm focus:outline-none focus:border-accent/30 focus:ring-1 focus:ring-accent/30 transition-all resize-none" required></textarea>
        </div>
        <p class="text-sm font-semibold text-center text-accent/80 mt-2 mb-2 italic">Your project deserves a presentation experience that sells before construction begins.</p>
        <button type="submit" class="w-full py-4 mt-2 bg-accent text-white font-bold rounded-xl hover:bg-accent-dark transition-all duration-200 shadow-xl shadow-accent/25 text-sm uppercase tracking-wider">Request Premium Consultation</button>
      </form>
    </div>
  </div>

  <!-- Ultra Premium Modal -->
  <div id="modal-ultra" class="fixed inset-0 z-[100] flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-300">
    <div class="absolute inset-0 bg-black/80 backdrop-blur-lg modal-bg-close"></div>
    <div class="relative bg-[#111] text-white w-full max-w-2xl rounded-2xl shadow-2xl p-8 transform scale-95 transition-transform duration-300 overflow-y-auto max-h-[90vh] modal-content-box border border-amber-300/30">
      <button class="absolute top-4 right-4 text-white/40 hover:text-white transition-colors modal-close-btn">
        <iconify-icon icon="lucide:x" class="text-xl"></iconify-icon>
      </button>
      <div class="flex items-center gap-2 mb-1">
        <iconify-icon icon="lucide:sparkles" class="text-amber-300 text-2xl"></iconify-icon>
        <h3 class="font-display text-3xl font-bold text-white">Ultra Premium Form</h3>
      </div>
      <p class="text-[11px] font-bold uppercase tracking-[0.2em] text-amber-300 mb-2">Enterprise / Cinematic Experience</p>
      <p class="text-sm text-white/50 mb-8">This form is elite and highly detailed. Designed for landmark developments.</p>
      
      <form class="space-y-5">
        <div class="grid grid-cols-2 gap-5">
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Full Name</label><input type="text" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Company / Group Name</label><input type="text" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Position / Role</label><input type="text" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all"></div>
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Direct Contact Number</label><input type="tel" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all" required></div>
          <div class="col-span-2"><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Business Email</label><input type="email" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all" required></div>
        </div>
        <div class="grid grid-cols-2 gap-5">
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Project Name</label><input type="text" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all" required></div>
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Total Project Area</label><input type="text" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all" required></div>
        </div>
        <div class="grid grid-cols-2 gap-5">
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Project Category</label>
            <select class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all [&>option]:text-black" required><option value="" disabled selected>Select category</option><option>Luxury Villas</option><option>Township</option><option>High-Rise</option><option>Commercial Landmark</option></select>
          </div>
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Preferred Visual Style</label>
            <select class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all [&>option]:text-black" required><option value="" disabled selected>Select style</option><option>Cinematic</option><option>Ultra Realistic</option><option>Luxury Modern</option><option>Architectural Minimal</option></select>
          </div>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-2">Elite Features Needed</label>
          <div class="grid grid-cols-2 gap-3 text-sm text-white/70">
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black/50 border-white/20 text-amber-300 focus:ring-amber-300 focus:ring-offset-gray-900"> Live Environment Simulation</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black/50 border-white/20 text-amber-300 focus:ring-amber-300 focus:ring-offset-gray-900"> VR Experience</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black/50 border-white/20 text-amber-300 focus:ring-amber-300 focus:ring-offset-gray-900"> AI Walkthrough</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black/50 border-white/20 text-amber-300 focus:ring-amber-300 focus:ring-offset-gray-900"> Interactive Map + POI</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black/50 border-white/20 text-amber-300 focus:ring-amber-300 focus:ring-offset-gray-900"> Investor Presentation Mode</label>
            <label class="flex items-center gap-2"><input type="checkbox" class="rounded bg-black/50 border-white/20 text-amber-300 focus:ring-amber-300 focus:ring-offset-gray-900"> Multi-Language Support</label>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-5">
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Expected Project Launch</label><input type="date" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all [&::-webkit-calendar-picker-indicator]:invert" required></div>
          <div><label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Estimated Budget Range</label><input type="text" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all" required></div>
        </div>
        <div>
          <label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Upload Master Plans / Branding Assets</label>
          <input type="file" multiple class="w-full text-sm text-white/50 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-bold file:bg-white/10 file:text-amber-300 hover:file:bg-white/20 transition-all">
        </div>
        <div>
          <label class="block text-[11px] font-bold text-white/50 uppercase tracking-wider mb-1.5">Additional Technical Requirements</label>
          <textarea rows="2" class="w-full px-3 py-2 bg-white/5 border border-white/10 rounded-lg text-sm text-white focus:outline-none focus:border-amber-300/50 focus:ring-1 focus:ring-amber-300/50 transition-all resize-none"></textarea>
        </div>
        <button type="submit" class="w-full py-4 mt-4 bg-amber-300 text-black font-bold rounded-xl hover:bg-amber-400 transition-all duration-200 shadow-[0_0_20px_rgba(252,211,77,0.3)] text-sm uppercase tracking-[0.15em]">Schedule Ultra Premium Consultation</button>
        <div class="flex items-center justify-center gap-4 text-[10px] font-bold uppercase tracking-[0.1em] text-white/40 mt-6 pt-4 border-t border-white/10">
          <span>Priority Response within 12 Hours</span>
          <span>&bull;</span>
          <span>Dedicated Project Consultation</span>
          <span>&bull;</span>
          <span>Confidential Project Handling</span>
        </div>
      </form>
    </div>
  </div>
"""

content = content.replace('<script>', new_modals + '\n  <script>')

old_js = '''
    // Modal Logic
    const modal = document.getElementById('project-modal');
    const modalContent = document.getElementById('modal-content');
    const startBtn = document.getElementById('start-project-btn');
    const closeBtn = document.getElementById('close-modal-btn');
    const backdrop = document.getElementById('modal-backdrop');

    const openModal = (e) => {
      e.preventDefault();
      modal.classList.remove('opacity-0', 'pointer-events-none');
      modalContent.classList.remove('scale-95');
      modalContent.classList.add('scale-100');
    };

    const closeModal = () => {
      modal.classList.add('opacity-0', 'pointer-events-none');
      modalContent.classList.remove('scale-100');
      modalContent.classList.add('scale-95');
    };

    startBtn.addEventListener('click', openModal);
    closeBtn.addEventListener('click', closeModal);
    backdrop.addEventListener('click', closeModal);
'''

new_js = '''
    // General Project Modal Logic
    const initModal = (modalId, btnId) => {
      const modal = document.getElementById(modalId);
      const btn = document.getElementById(btnId);
      if (!modal || !btn) return;
      
      const modalContent = modal.querySelector('.modal-content-box') || document.getElementById('modal-content');
      const closeBtns = modal.querySelectorAll('.modal-close-btn, #close-modal-btn');
      const backdrop = modal.querySelector('.modal-bg-close') || document.getElementById('modal-backdrop');

      const openModal = (e) => {
        e.preventDefault();
        modal.classList.remove('opacity-0', 'pointer-events-none');
        if(modalContent) {
          modalContent.classList.remove('scale-95');
          modalContent.classList.add('scale-100');
        }
      };

      const closeModal = () => {
        modal.classList.add('opacity-0', 'pointer-events-none');
        if(modalContent) {
          modalContent.classList.remove('scale-100');
          modalContent.classList.add('scale-95');
        }
      };

      btn.addEventListener('click', openModal);
      closeBtns.forEach(b => b.addEventListener('click', closeModal));
      if(backdrop) backdrop.addEventListener('click', closeModal);
    };

    initModal('project-modal', 'start-project-btn');
    initModal('modal-standard', 'btn-standard');
    initModal('modal-deluxe', 'btn-deluxe');
    initModal('modal-premium', 'btn-premium');
    initModal('modal-ultra', 'btn-ultra');
'''

content = content.replace(old_js.strip(), new_js.strip())

with open(file_path, 'w') as f:
    f.write(content)
