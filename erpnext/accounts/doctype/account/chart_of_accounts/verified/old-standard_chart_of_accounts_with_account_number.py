# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
from frappe import _

def get():
    return {
	    "Aset" : {
	      "root_type" : "Asset",
	      "account_number" : "1",
	      "Aset Lancar" : {
	        "account_number" : "11",
	        "Kas" : {
	          "account_number" : "111",
	          "Kas Kecil (Rp)" : {
	            "account_type" : "Cash",
	            "account_number" : "111-010"
	          },
	          "Kas Besar (Rp)" : {
	            # "account_type" : "Cash",
	            "account_number" : "111-020"
	          }
	        },
	        "Bank" : {
	          "account_number" : "112",
	          "Bank 1" : {
	            "account_type" : "Bank",
	            "account_number" : "112-010"
	          }
	        },
	        "Piutang Usaha" : {
	          "account_number" : "113",
	          "Piutang Dagang 1" : {
	            "account_type" : "Receivable",
	            "account_number" : "113-010"
	          }
	        },
	        "Pendapatan Yang Akan di Terima" : {
	          "account_number" : "114",
	          "Penyewaan Belum Diterima" : {
	            # "account_type" : "Receivable",
	            "account_number" : "114-010"
	          },
	          "Pendapatan Komisi" : {
	            # "account_type" : "Receivable",
	            "account_number" : "114-020"
	          }
	        },
	        "Piutang Lain-lain" : {
	          "account_number" : "115",
	          "Pinjaman Karyawan" : {
	            # "account_type" : "Receivable",
	            "account_number" : "115-010"
	          },
	          "Piutang Lainnya" : {
	            # "account_type" : "Receivable",
	            "account_number" : "115-900"
	          }
	        },
	        "Persediaan Barang" : {
	          "account_number" : "116",
	          "Persediaan Barang Jadi" : {
	            "account_type" : "Stock",
	            "account_number" : "116-010"
	          },
	          "Persediaan Barang Setengah Jadi" : {
	            "account_type" : "Stock",
	            "account_number" : "116-020"
	          },
	          "Persediaan Bahan Baku" : {
	            "account_type" : "Stock",
	            "account_number" : "116-030"
	          },
	          "Persediaan Lainnya" : {
	            "account_type" : "Stock",
	            "account_number" : "116-090"
	          },
	           "Uang Muka Pembelian Barang" : {
	            "account_number" : "116-110"
	          }
	       },
	        "Biaya Bayar Dimuka" : {
	          "account_number" : "117",
	          "Sewa Bayar Dimuka" : {
	            "account_number" : "117-010"
	          },
	          "Asuransi Bayar Dimuka" : {
	            "account_number" : "117-020"
	          },
	          "Perijinan Bayar Dimuka" : {
	            "account_number" : "117-030"
	          },
	          "Pajak Bayar Dimuka" : {
	            "account_number" : "117-040"
	          }
	        },
	        "Biaya Provisi dan Admin Bank" : {
	          "account_number" : "118",
	          "Biaya Provisi" : {
	            "account_number" : "118-010"
	          },
	          "Biaya Administrasi" : {
	            "account_number" : "118-020"
	          },
	          "Biaya Notaris" : {
	            "account_number" : "118-030"
	          }
	        },
	        "Aset Lancar Lain-lain" : {
	          "account_number" : "119",
	          "Akun Sementara" : {
	            "account_type" : "Temporary",
	            "account_number" : "119-010"
	          },
	          "Aset Lancar Lainnya" : {
	            "account_number" : "119-900"
	          }
	        }
	      },
	      "Aset Tetap" : {
	        "account_number" : "12",
	        "Tanah" : {
	          "account_number" : "121",
	          "Tanah" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "121-010"
	          }
	        },
	        "Bangunan" : {
	          "account_number" : "122",
	          "Bangunan Kantor" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "122-010"
	          },
	          "Bangunan Tempat Usaha" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "122-020"
	          },
	          "Bangunan Gudang" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "122-030"
	          }
	        },
	        "Kendaraan" : {
	          "account_number" : "123",
	          "Kendaraan Operasional" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "123-010"
	          },
	          "Kendaraan Dinas" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "123-020"
	          }
	        },
	        "Peralatan" : {
	          "account_number" : "124",
	          "Peralatan Kantor" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "124-010"
	          },
	          "Peralatan Tempat Usaha" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "124-020"
	          },
	          "Peralatan Gudang " : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "124-030"
	          },
	          "Peralatan Kendaraan " : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "124-040"
	          }
	        },
	        "Aset Tak Berwujud" : {
	          "account_number" : "125",
	          "Biaya Pra Operasi" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "125-010"
	          },
	          "Paten" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "125-020"
	          },
	          "Merek Dagang" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "125-030"
	          },
	          "Perijinan" : {
	            "account_type" : "Fixed Asset",
	            "account_number" : "125-040"
	          }
	        },
	        "Investasi" : {
	          "account_number" : "126",
	          "Deposito" : {
	            "account_number" : "126-010"
	          },
	          "Investasi Saham" : {
	            "account_number" : "126-020"
	          },
	          "Investasi Perumahan" : {
	            "account_number" : "126-030"
	          }
	        },
	        "Akumulasi Penyusutan dan Amortisasi" : {
	          "account_number" : "127",
	          "Akumulasi Penyusutan Bangunan" : {
	            "account_type" : "Accumulated Depreciation",
	            "account_number" : "127-010"
	          },
	          "Akumulasi Penyusutan Kendaraan" : {
	            # "account_type" : "Accumulated Depreciation",
	            "account_number" : "127-110"
	          },
	          "Akumulasi Penyusutan Peralatan" : {
	            # "account_type" : "Accumulated Depreciation",
	            "account_number" : "127-210"
	          },
	          "Akumulasi Amortisasi Aset Tak Berwujud" : {
	            # "account_type" : "Accumulated Depreciation",
	            "account_number" : "127-310"
	          }
	        },
	        "Aset Tetap Lain-lain" : {
	          "account_number" : "129",
	          "Aset Tetap Lainnya" : {
	            "account_number" : "129-900"
	          }
	        }
	      }
	    },
	    "Kewajiban" : {
	      "account_number" : "2",
	      "root_type" : "Liability",
	      "Kewajiban Jangka Pendek" : {
	        "account_number" : "21",
	        "Hutang Dagang" : {
	          "account_number" : "211",
	          "Hutang Dagang" : {
	            "account_type" : "Payable",
	            "account_number" : "211-010"
	          }
	        },
	        "Pendapatan di Terima di Muka" : {
	          "account_number" : "212",
	          "Penerimaan Uang Muka Penjualan" : {
	            "account_number" : "212-010"
	          },
	          "Pendapatan Sewa Diterima Dimuka" : {
	            "account_number" : "212-020"
	          }
	        },
	        "Persediaan Diterima Tapi Tidak Ditagih" : {
	          "account_number" : "213",
	          "Persediaan Diterima Tidak Ditagih" : {
	            "account_type" : "Stock Received But Not Billed",
	            "account_number" : "213-010"
	          }
	        },
	        "Biaya Yang Akan di Bayar" : {
	          "account_number" : "214",
	          "Biaya Akan Dibayar - Gaji" : {
	            # "account_type" : "Payable",
	            "account_number" : "214-010"
	          },
	          "Biaya Akan Dibayar - Bonus, THR" : {
	            # "account_type" : "Payable",
	            "account_number" : "214-020"
	          },
	          "Biaya Akan Dibayar - PLN, PAM dan Telepon" : {
	            # "account_type" : "Payable",
	            "account_number" : "214-030"
	          },
	          "Biaya Akan Dibayar - Pengiriman" : {
	            # "account_type" : "Payable",
	            "account_number" : "214-040"
	          },
	          "Biaya Akan Dibayar - Pajak" : {
	            # "account_type" : "Payable",
	            "account_number" : "214-050"
	          },
	          "Biaya Akan Dibayar - Bunga Pada Pihak Ke-3" : {
	            # "account_type" : "Payable",
	            "account_number" : "214-060"
	          },
	          "Biaya Akan Dibayar - Lain lain" : {
	            # "account_type" : "Payable",
	            "account_number" : "214-900"
	          }
	        },
	        "Hutang Pajak" : {
	          "account_number" : "215",
	          "PPN Keluaran" : {
	            # "account_type" : "Payable",
	            "account_number" : "215-010"
	          },
	          "Hutang Pajak Final" : {
	            # "account_type" : "Payable",
	            "account_number" : "215-020"
	          },
	          "Hutang Pajak PPh 22" : {
	            # "account_type" : "Payable",
	            "account_number" : "215-030"
	          },
	          "Hutang Pajak PPh 23" : {
	            # "account_type" : "Payable",
	            "account_number" : "215-040"
	          },
	          "Hutang Pajak PPh 25" : {
	            # "account_type" : "Payable",
	            "account_number" : "215-050"
	          },
	          "Hutang Pajak Lainnya" : {
	            # "account_type" : "Payable",
	            "account_number" : "215-900"
	          }
	        },
	        "Kewajiban Lancar Lain-lain" : {
	          "account_number" : "219",
	          "Hutang Lancar Lainnya" : {
	            # "account_type" : "Payable",
	            "account_number" : "219-900"
	          }
	        }
	      },
	      "Kewajiban Jangka Panjang" : {
	        "account_number" : "22",
	        "Pinjaman" : {
	          "account_number" : "221",
	          "Pinjaman Dari Bank" : {
	            "account_number" : "221-010"
	          },
	          "Pinjaman Dari Pihak Lain" : {
	            "account_number" : "221-020"
	          }
	        },
	        "Hutang Pembelian Secara Kredit" : {
	          "account_number" : "222",
	          "Hutang Cicilan Kendaraan" : {
	            "account_number" : "222-010"
	          },
	          "Hutang Cicilan Properti" : {
	            "account_number" : "222-020"
	          }
	        },
	        "Hutang Bunga Pinjaman" : {
	          "account_number" : "223",
	          "Hutang Bunga Pinjaman Bank" : {
	            "account_number" : "223-010"
	          },
	          "Hutang Bunga Pinjaman Pada Pihak Lain" : {
	            "account_number" : "223-020"
	          },
	          "Hutang Bunga Pembelian Secara Kredit" : {
	            "account_number" : "223-030"
	          },
	          "Hutang Bunga Lainnya" : {
	            "account_number" : "223-900"
	          }
	        },
	        "Kewajiban Jangka Panjang Lain-lain" : {
	          "account_number" : "229",
	          "Hutang Jangka Panjang Lainnya" : {
	            "account_number" : "229-900"
	          }
	        }
	      }
	    },
	    "Ekuitas" : {
	      "account_number" : "3",
	      "root_type" : "Equity",
	      "Modal" : {
	        "account_number" : "31",
	        "Permodalan" : {
	          "account_number" : "311",
	          "Saldo Awal Ekuitas" : {
	            "account_type" : "Equity",
	            "account_number" : "311-010"
	          },
	          "Modal Disetor Oleh Pemilik" : {
	            "account_type" : "Equity",
	            "account_number" : "311-020"
	          },
	          "Modal Bantuan/Hibah" : {
	            "account_type" : "Equity",
	            "account_number" : "311-030"
	          },
	          "Pengambilan Modal Oleh Pemilik" : {
	            "account_type" : "Equity",
	            "account_number" : "311-110"
	          }
	        }
	      },
	      "Laba" : {
	        "account_number" : "32",
	        "Laba" : {
	          "account_number" : "321",
	          "Laba Tahun Berjalan" : {
	            "account_type" : "Equity",
	            "account_number" : "321-010"
	          },
	          "Laba Periode Berjalan" : {
	            "account_type" : "Equity",
	            "account_number" : "321-020"
	          },
	          "Laba di Tahan" : {
	            "account_type" : "Equity",
	            "account_number" : "321-030"
	          }
	        }
	      }
	    },
	    "Pendapatan" : {
	      "account_number" : "4",
	      "root_type" : "Income",
	      "Pendapatan Usaha" : {
	        "account_number" : "41",
	        "Penjualan" : {
	          "account_number" : "411",
	          "Penjualan Jasa" : {
	            "account_type" : "Income Account",
	            "account_number" : "411-010"
	          },
	          "Penjualan Barang" : {
	            "account_type" : "Income Account",
	            "account_number" : "411-050"
	          }
	        },
	        "Retur dan Diskon Penjualan" : {
	          "account_number" : "412",
	          "Retur Penjualan" : {
	            "account_number" : "412-010"
	          },
	          "Potongan Penjualan" : {
	            "account_number" : "412-020"
	          }
	        }
	      },
	      "Pendapatan Non-Usaha" : {
	        "account_number" : "42",
	        "Pendapatan Lain lain" : {
	          "account_number" : "421",
	          "Pendapatan Komisi" : {
	            "account_type" : "Income Account",
	            "account_number" : "421-010"
	          },
	          "Pendapatan Sewa" : {
	            "account_type" : "Income Account",
	            "account_number" : "421-020"
	          },
	          "Pendapatan Ongkos Penjualan" : {
	            "account_type" : "Income Account",
	            "account_number" : "421-030"
	          },
	          "Pendapatan Bunga Bank" : {
	            "account_type" : "Income Account",
	            "account_number" : "421-110"
	          },
	          "Pendapatan Bunga Dari Pihak Lain" : {
	            "account_type" : "Income Account",
	            "account_number" : "421-120"
	          },
	          "Pendapatan Keuntungan Penjualan Aset" : {
	            "account_type" : "Income Account",
	            "account_number" : "421-510"
	          },
	          "Pendapatan Non-Usaha Lainnya" : {
	            "account_type" : "Income Account",
	            "account_number" : "421-900"
	          }
	        }
	      }
	    },
	    "Beban dan Biaya" : {
	      "account_number" : "5",
	      "root_type" : "Expense",
	      "Harga Pokok Penjualan" : {
	        "account_number" : "51",
	        "Biaya Langsung" : {
	          "account_number" : "511",
	          "account_type" : "Cost of Goods Sold",
	          "Biaya Upah Buruh & Kuli Angkut" : {
	            "account_number" : "511-010"
	          },
	          "Biaya Kemasan & Pengiriman" : {
	            "account_type" : "Expenses Included In Valuation",
	            "account_number" : "511-020"
	          },
	          "Potongan Oleh Pemasok" : {
	            "account_number" : "511-030"
	          }
	        },
	        "Biaya Tidak Langsung" : {
	          "account_number" : "512",
	          "Biaya Perjalanan Dinas" : {
                "account_type" : "Cost of Goods Sold",
	            "account_number" : "512-010"
	          },
	          "Biaya Iklan & Promosi" : {
	            "account_number" : "512-020"
	          },
	          "Biaya Iuran Bulanan" : {
	            "account_number" : "512-030"
	          },
	          "Beban Bonus, Hadiah & Sampel" : {
	            "account_number" : "512-040"
	          },
	          "Beban Komisi" : {
	            "account_number" : "512-050"
	          },
	          "Beban Barang Susut & Rusak" : {
	            "account_number" : "512-060"
	          },
	          "Penyesuaian Persediaan" : {
	            "account_type" : "Stock Adjustment",
	            "account_number" : "512-070"
	          },
	          "Beban Piutang Tak Tertagih" : {
	            "account_number" : "512-080"
	          },
	          "Biaya Perbaikan" : {
	            "account_number" : "512-090"
	          },
	          "Biaya & Beban Penjualan Lainnya" : {
	            "account_number" : "512-900"
	          }
	        }
	      },
	      "Biaya Operasional" : {
	        "account_number" : "52",
	        "Biaya Gaji & Kesejahteraan Pegawai" : {
	          "account_number" : "521",
	          "Biaya Gaji Staff & Karyawan Tetap" : {
	            "account_number" : "521-010"
	          },
	          "Biaya Gaji Karyawan Kontrak & Harian" : {
	            "account_number" : "521-020"
	          },
	          "Biaya Konsumsi" : {
	            "account_number" : "521-030"
	          },
	          "Biaya Pengobatan" : {
	            "account_number" : "521-040"
	          },
	          "Biaya THR & Bonus" : {
	            "account_number" : "521-050"
	          },
	          "Biaya Asuransi Pegawai" : {
	            "account_number" : "521-060"
	          },
	          "Biaya Gaji & Kesejahteraan Lainnya" : {
	            "account_number" : "521-900"
	          }
	        },
	        "Biaya Operasional Usaha" : {
	          "account_number" : "522",
	          "Biaya ATK, Fotokopi, Foto, Cetak" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-010"
	          },
	          "Biaya Telpon, Fax, Internet" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-020"
	          },
	          "Biaya Listrik & Air" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-030"
	          },
	          "Biaya Kirim Dokumen, Meterai, Pos" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-040"
	          },
	          "Biaya BBM, Tol, Parkir Lainnya" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-050"
	          },
	          "Biaya Humas & Pemasaran" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-060"
	          },
	          "Biaya Sumbangan & Iuran Bulanan" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-070"
	          },
	          "Biaya Perjalanan Dinas" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-080"
	          },
	          "Biaya Operasional Lainnya" : {
	            "account_type" : "Expense Account",
	            "account_number" : "522-900"
	          }
	        }
	      },
	      "Biaya Non Operasional" : {
	        "account_number" : "53",
	        "Biaya Non Operasional" : {
	          "account_number" : "531",
	          "Biaya Administrasi Bank" : {
	            "account_type" : "Chargeable",
	            "account_number" : "531-110"
	          },
	          "Biaya Provisi Pinjaman bank" : {
	            "account_type" : "Chargeable",
	            "account_number" : "531-120"
	          },
	          "Biaya Notaris" : {
	            "account_type" : "Chargeable",
	            "account_number" : "531-130"
	          },
	          "Biaya Sewa" : {
	            "account_type" : "Expense Account",
	            "account_number" : "531-140"
	          },
	          "Biaya Peralatan" : {
	            "account_type" : "Expense Account",
	            "account_number" : "531-150"
	          },
	          "Biaya Pemeliharaan" : {
	            "account_type" : "Expense Account",
	            "account_number" : "531-160"
	          },
	          "Biaya Asuransi" : {
	            "account_type" : "Expense Account",
	            "account_number" : "531-170"
	          },
	          "Biaya Perijinan" : {
	            "account_type" : "Expense Account",
	            "account_number" : "531-180"
	          }
	        },
	        "Beban Bunga dan Pajak" : {
	          "account_number" : "532",
	          "Beban Bunga Kredit Rekening Koran Bank" : {
	            "account_type" : "Tax",
	            "account_number" : "532-010"
	          },
	          "Beban Bunga Pinjaman Pada Pihak Ke 3" : {
	            "account_type" : "Tax",
	            "account_number" : "532-020"
	          },
	          "Beban Pajak Bumi & Bangunan" : {
	            "account_type" : "Tax",
	            "account_number" : "532-030"
	          },
	          "Beban Pajak Penghasilan" : {
	            "account_type" : "Tax",
	            "account_number" : "532-040"
	          },
	          "Beban Pajak PPN" : {
	            "account_type" : "Tax",
	            "account_number" : "532-050"
	          },
	          "Beban Pajak Lainnya" : {
	            "account_type" : "Tax",
	            "account_number" : "532-900"
	          }
	        },
	        "Beban Penyusutan & Amortisasi" : {
	          "account_number" : "533",
	          "Beban Penyusutan Bangunan" : {
	            "account_type" : "Depreciation",
	            "account_number" : "533-010"
	          },
	          "Beban Penyusutan Kendaraan" : {
	            # "account_type" : "Depreciation",
	            "account_number" : "533-110"
	          },
	          "Beban Penyusutan Peralatan" : {
	            # "account_type" : "Depreciation",
	            "account_number" : "533-210"
	          },
	          "Beban Amortisasi Aset Tak Berwujud" : {
	            # "account_type" : "Depreciation",
	            "account_number" : "533-310"
	          }
	        },
	        "Biaya & Beban Lain-lain" : {
	          "account_number" : "539",
	          "Selisih Pembayaran Pembeli" : {
	            "account_type" : "Round Off",
	            "account_number" : "539-010"
	          },
	          "Selisih Kurs" : {
	            # "account_type" : "Round Off",
	            "account_number" : "539-020"
	          },
	          "Kerugian Penjualan Aset Tetap" : {
	            "account_number" : "539-030"
	          },
	          "Penghapusan (Write-Off)" : {
	            "account_number" : "539-040"
	          },
	          "Kerugian Bencana" : {
	            "account_number" : "539-050"
	          }
	        }
	      }
	    }
	  }
